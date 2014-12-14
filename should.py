# -*- coding: utf-8 -*-

from functools import partial
from contextlib import contextmanager

_just_chains = ['an', 'of', 'a', 'be', 'which', 'also', 'as']

_not_chains = ['no']

_basic_types = [bool, int, str, list, tuple, dict]


class _Should(object):


    def __init__(self, val=None):
        self._val = val
        self._not = False  # `not` flag

        self._set_property(_just_chains, self._chain)
        self._set_property(_not_chains, self._set_not)

        for t in _basic_types:
            p = property(fget=partial(self._types, t))
            setattr(self.__class__, t.__name__, p)

    @staticmethod
    @contextmanager
    def raises(exception):
        '''
        异常的断言
        @param {Exception} exception 需要抛出的异常
        '''
        try:
            yield
        except exception:
            pass
        else:
            assert False, 'should raise ' + exception.__name__

    @classmethod
    def _set_property(cls, lst, fget, fset=None):
        for name in lst:
            p = property(fget=fget, fset=fset)
            setattr(cls, name, p)

    def _set_not(self, cls):
        self._not = True
        return self

    def _chain(self, cls):
        return self

    @property
    def _flag(self):
        return not self._not and 'not ' or ''

    def _assert(self, res, msg):
        ''' 统一的 assert 方法, 每次断言之后取消取否 '''
        assert res, msg
        self._not = False

    def _types(self, ttype, cls):
        res, msg = self.__types(ttype, self._val)
        self._assert(res, msg)
        return self

    def equal(self, value):
        res, msg = self._equal(value, self._val)
        self._assert(res, msg)
        return self

    def less(self, value):
        res, msg = self._less(value, self._val)
        self._assert(res, msg)
        return self

    def greater(self, value):
        res, msg = self._greater(value, self._val)
        self._assert(res, msg)
        return self

    def contain(self, value):
        res, msg = self._contain(value, self._val)
        self._assert(res, msg)

    @property
    def ok(self):
        res, msg = self._ok(self._val)
        self._assert(res, msg)
        return self

    def __types(self, exp, value):
        actual = type(value)
        res = (actual is not exp) if self._not else (actual is exp)
        msg = '{0} is {1}{2}'.format
        return res, msg(value, self._flag, exp)

    def _ok(self, actual):
        res = not bool(actual) if self._not else bool(actual)
        msg = '{0}\'s bool value is {1}True'.format
        return res, msg(actual, self._flag)

    def _equal(self, exp, actual):
        res = (actual != exp) if self._not else (actual == exp)
        msg = '{0} is {1}equal {2}'.format
        return res, msg(actual, self._flag, exp)

    def _less(self, exp, actual):
        res = (actual >= exp) if self._not else (actual < exp)
        msg = '{0} is {1}less than {2}'.format
        return res, msg(actual, self._flag, exp)

    def _greater(self, exp, actual):
        res = (actual <= exp) if self._not else (actual > exp)
        msg = '{0} is {1}greater than {2}'.format
        return res, msg(actual, self._flag, exp)

    def _contain(self, exp, actual):
        res = (exp not in actual) if self._not else (exp in actual)
        msg = '{0} is {1}contain {2}'.format
        return res, msg(actual, self._flag, exp)


should = _Should
