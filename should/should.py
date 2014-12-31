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
import re
import sys

PY3 = sys.version_info[0] == 3

if not PY3:
    reload(sys)
    sys.setdefaultencoding('utf8')


_basic_types = list(filter(lambda t: type(t) is type, __builtins__.values()))
_basic_types.remove(property)

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
    # it('a').should.be.instanceof(basestring)
    'instanceof': lambda exp, actual: isinstance(actual, exp),
    # it('string').should.match(r'tr.')
    'match': lambda exp, actual: re.search(exp, actual) is not None,
    # it('string').should.search(r'tr.')
    'search': lambda exp, actual: re.search(exp, actual) is not None
}


class _ChainMeta(object):

    def __new__(cls, name, bases, attrs):
        chain = property(lambda self: self)
        names = ['should', 'have', 'an', 'of', 'a', 'be', 'also', 'which']
        attrs.update({}.fromkeys(names, chain))
        return type(name, bases, attrs)


class Chain(object):
    __metaclass__ = _ChainMeta


class Should(object):

    def __init__(self, val=None):
        self._val = val
        self._not = False  # `not` flag

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

    @property
    def no(self):
        '''断言取反'''
        self._not = True
        return self

    def _assert(self, res, msg):
        ''' 统一的 assert 方法, 每次断言之后取消取否 '''
        assert res, msg
        self._not = False

    @property
    def _flag(self):
        return 'not ' if self._not else ''

    def use(self, cls):
        origin = self.__class__
        self.__class__ = type('shouldobj', (cls, origin), {})
        return self

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
        msg_format = '{0} should {1}{2} {3}'.format
        if self._not:
            res = not res
        msg = msg_format(self._val, self._flag, assertion, exp)
        self._assert(res, msg)
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
