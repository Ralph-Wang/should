# -*- coding: utf-8 -*-

from functools import partial
from contextlib import contextmanager
import re
import sys


# compact 3.*
if 'basestring' not in __builtins__:
    basestring = str

_just_chains = {
    'should': None, 'have': 'have', 'an': None, 'of': None,
    'a': None, 'be': 'be', 'also': None
}

_not_chains = {'no': None}

_basic_types = list(filter(lambda t: type(t) is type, __builtins__.values()))

# which 有别的用处

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
    'key': lambda exp, actual: exp in actual.keys(),
    'instanceof': lambda exp, actual: isinstance(actual, exp),
    'match': lambda exp, actual: re.search(exp, actual) is not None,
    'search': lambda exp, actual: re.search(exp, actual) is not None
}


class _Should(object):

    def __init__(self, val=None):
        self._val = val
        self._conj = ''
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
        if isinstance(exception, basestring):
            exe_msg = exception
            exception = Exception
            msg = ('should {0}raise msg:' + exe_msg).format
        else:
            exe_msg = None
            msg = ('should {0}raise ' + exception.__name__).format

        try:
            self._val()
        except exception as e:
            res = True
            if exe_msg is not None:
                res = exe_msg in str(e)
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
            sys.stderr.write(
                'raises will be deprecated in 0.5, use throw please.\n')
        except exception:
            pass
        else:
            assert False, 'should raise ' + exception.__name__

    @classmethod
    def _set_property(cls, dct, fget, fset=None):
        for name, conj in dct.items():
            p = property(fget=partial(fget, conj), fset=fset)
            setattr(cls, name, p)

    def _set_not(self, conj=None, cls=None):
        self._conj = self._conj if conj is None else conj
        self._not = True
        return self

    def _chain(self, conj='be', cls=None):
        self._conj = self._conj if conj is None else conj
        return self

    @property
    def _flag(self):
        return 'not ' if self._not else ''

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
        msg_format = '{0} should {1}{2} {3} {4}'.format
        if self._not:
            res = not res
        msg = msg_format(self._val, self._flag, self._conj, assertion, exp)
        self._assert(res, msg)
        return self

    @property
    def ok(self):
        res, msg = self._ok(self._val)
        self._assert(res, msg)
        return self

    @property
    def empty(self):
        self.length(0)
        return self

    def __values(self, exp, actual):
        res = (actual is not exp) if self._not else (actual is exp)
        msg_format = '{0} should be {1}{2}'.format
        return res, msg_format(actual, self._flag, exp)

    def __types(self, exp, value):
        actual = type(value)
        res = (actual is not exp) if self._not else (actual is exp)
        msg_format = '{0} should be {1}{2}'.format
        return res, msg_format(value, self._flag, exp)

    def _ok(self, actual):
        res = not bool(actual) if self._not else bool(actual)
        msg_format = '{0}\'s bool value is {1}True'.format
        return res, msg_format(actual, self._flag)


should = _Should
it = _Should
