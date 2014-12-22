# -*- coding: utf-8 -*-

'''
should.py:
    BDD assertion library

    Sample:
        >>> from should import it
        >>> it(1).should.be.int.also.be.equal(1)
        >>> it(lambda: foo()).should.throw(ValueError)
        >>> it(lambda: foo()).should.throw("Some Message")
'''

from functools import partial
from contextlib import contextmanager
import re
import sys


_just_chains = {
    'should': None, 'have': 'have', 'an': None, 'of': None,
    'a': None, 'be': 'be', 'also': None, 'which': None
}

_not_chains = {'no': None}

_basic_types = list(filter(lambda t: type(t) is type, __builtins__.values()))

# boolean 值和 None 的断言可以简化为 it(True).should.be.true
_basic_values = {
    'true': True,
    'false': False,
    'none': None
}

# 所有的单值断言
_assertions = {
        # it([1]).should.contain(1)
    'contain': lambda exp, actual: exp in actual,
        # it(1).should.be.equal(1)
    'equal': lambda exp, actual: actual == exp,
        # it(5).should.be.less(7)
    'less': lambda exp, actual: actual < exp,
        # it(5).should.be.greater(3)
    'greater': lambda exp, actual: actual > exp,
        # it('abcdefg').should.be.startswith('abc')
    'startswith': lambda exp, actual: actual.startswith(exp),
        # it('abcdefg').should.be.endswith('defg')
    'endswith': lambda exp, actual: actual.endswith(exp),
        # it('abc').should.be.length(3)
    'length': lambda exp, actual: len(actual) == exp,
        # it({'a': 1}).should.have.key('a')
    'key': lambda exp, actual: exp in actual.keys(),
        # it('a').should.be.instanceof(basestring)
    'instanceof': lambda exp, actual: isinstance(actual, exp),
        # it('string').should.match(r'tr.')
    'match': lambda exp, actual: re.search(exp, actual) is not None,
        # it('string').should.search(r'tr.')
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
        '''
        异常断言.
        Sample:
            >>> it(lambda: foo()).should.throw(ValueError)
            >>> it(lambda: foo()).should.throw("Error Message")
        '''
        # compact 3.*
        try:
            basestring
        except NameError:
            basestring = str
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
        '''
        单纯用来做链式调用的属性
        '''
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

    def within(self, less, greater):
        '''
        范围断言, 值在 less, greater 之间
        '''
        res = less <= self._val <= greater
        msg_format = '{0} should be {1}within {2}, {3}'.format
        if self._not:
            res = not res
        msg = msg_format(self._val, self._flag, less, greater)
        self._assert(res, msg)
        return self

    @property
    def ok(self):
        '''
        boolean 断言, 值的布尔值为 True
        Sample:
            >>> it(1).should.be.ok
            >>> it(0).should.be.no.ok
        '''
        res, msg = self._ok(self._val)
        self._assert(res, msg)
        return self

    @property
    def empty(self):
        '''
        断言容器为空
        Sample:
            >>> it({}).should.be.empty
            >>> it([]).should.be.empty
            >>> it([1]).should.be.no.empty
        '''
        self.length(0)
        return self

    def proper(self, name):
        self.__property(name, False)
        return self

    def own_proper(self, name):
        self.__property(name, True)
        return self

    def __property(self, name, own=False):
        if own:
            pps = self._val.__dict__.keys()
        else:
            pps = dir(self._val)
        res = name in pps
        msg_format = '{0} should{1} have {2}property {3}'.format
        if self._not:
            res = not res
        msg = msg_format(self._val, self._flag, 'own ' if own else '', name)
        self._assert(res, msg)
        # 修改链式调用中需要断言的值
        self._val = getattr(self._val, name)
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
