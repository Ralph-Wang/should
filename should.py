# -*- coding: utf-8 -*-

from functools import partial
from contextlib import contextmanager
import sys

_just_chains = ['should', 'have', 'an', 'of', 'a', 'be', 'which', 'also', 'as']

_not_chains = ['no']

_basic_types = [bool, int, str, list, tuple, dict]

_basic_values = {
        'true': True,
        'false': False,
        'none': None
        }

_assertions = {
        'contain': lambda exp, actual: exp in actual,
        'equal': lambda exp, actual: actual == exp,
        'less': lambda exp, actual: actual < exp,
        'greater': lambda exp, actual: actual > exp,
        'startswith': lambda exp, actual: actual.startswith(exp),
        'endswith': lambda exp, actual: actual.endswith(exp),
        'length': lambda exp, actual: len(actual) == exp,
        'key': lambda exp, actual: exp in actual.keys()
        }


class _Should(object):


    def __init__(self, val=None):
        self._val = val
        self._not = False  # `not` flag

        self._set_property(_just_chains, self._chain)
        self._set_property(_not_chains, self._set_not)

        # 初始化断言
        for v in _basic_values:
            p = property(fget=partial(self._values, _basic_values[v]))
            setattr(self.__class__, v, p)

        for t in _basic_types:
            p = property(fget=partial(self._types, t))
            setattr(self.__class__, t.__name__, p)

        for assertion in _assertions:
            p = partial(self._assertions, assertion)
            setattr(self, assertion, p)

    def throw(self, exception):
        msg = ('should {0}raise ' + exception.__name__).format
        try:
            self._val()
        except exception:
            res = True
        else:
            res = False
        if self._not:
            res = not res
        self._assert(res, msg(self._flag))
        return self

    @staticmethod
    @contextmanager
    def raises(exception):
        '''
        异常的断言, 会在 0.5 废弃
        @param {Exception} exception 需要抛出的异常
        '''
        try:
            yield
            sys.stderr.write('raises will be deprecated in 0.5, use throw please.\n')
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
        return '' if self._not else 'not '

    def _assert(self, res, msg):
        ''' 统一的 assert 方法, 每次断言之后取消取否 '''
        assert res, msg
        self._not = False

    def _values(self, value, cls):
        res, msg = self.__values(value, self._val)
        self._assert(res, msg)
        return self

    def _types(self, ttype, cls):
        res, msg = self.__types(ttype, self._val)
        self._assert(res, msg)
        return self

    def _assertions(self, assertion, exp):
        res = _assertions[assertion](exp, self._val)
        msg = '{0} should {1}{2} {3}'.format
        if self._not:
            res = not res
        self._assert(res, msg(self._val, self._flag, assertion, exp))
        return self

    @property
    def ok(self):
        res, msg = self._ok(self._val)
        self._assert(res, msg)
        return self

    def __values(self, exp, actual):
        res = (actual is not exp) if self._not else (actual is exp)
        msg = '{0} is {1}{2}'.format
        return res, msg(actual, self._flag, exp)

    def __types(self, exp, value):
        actual = type(value)
        res = (actual is not exp) if self._not else (actual is exp)
        msg = '{0} is {1}{2}'.format
        return res, msg(value, self._flag, exp)

    def _ok(self, actual):
        res = not bool(actual) if self._not else bool(actual)
        msg = '{0}\'s bool value is {1}True'.format
        return res, msg(actual, self._flag)


should = _Should
it = _Should
