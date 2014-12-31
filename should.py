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


class _Should(object):

    def __init__(self, val=None):
        self._val = val
        self._conj = ''
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

    def use(self, cls):
        origin = self.__class__
        self.__class__ = type('shouldobj', (cls, origin), {})
        return self

    def throw(self, exception):
        '''
        异常断言.
        Sample:
            >>> it(lambda: foo()).should.throw(ValueError)
            >>> it(lambda: foo()).should.throw("Error Message")
        '''
        if str(exception) == exception:
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

    raises = throw

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

    def key(self, name):
        '''
        键值断言. 针对字典的键. 会改变链式调用的断言值.
        不存在的 key 会将链式调用值变为 None
        Sample:
            >>> it({'a':1, 'b':2}).should.have.key('a').which.should.be.equal(1)
            >>> it({'a':1, 'b':2}).should.have.key('c').which.should.be.none
        '''
        self.__key(name)
        self._val = self._val.get(name, None)
        return self

    def keys(self, *args):
        '''
        键值列表断言. 针对字典的键
        Sample:
            >>> it({'a':1, 'b':2}).should.have.keys('a', 'b')
            >>> it({'a':1, 'b':2}).should.have.keys(['a', 'b'])
        '''
        keys = []
        for i in args:
            if isinstance(i, list):
                keys.extend(i)
            else:
                keys.append(i)

        for key in keys:
            self.__key(key)
        return self

    def proper(self, name):
        self.__property(name, False)
        # 修改链式调用中需要断言的值
        self._val = getattr(self._val, name, None)
        return self

    property = proper

    def own_proper(self, name):
        self.__property(name, True)
        # 修改链式调用中需要断言的值
        self._val = getattr(self._val, name, None)
        return self

    own_property = own_proper

    def properties(self, *args):
        '''
        属性列表断言. 包含类属性以及继承得到的属性
        Samle:
            >>> it(obj).should.have.properties('a', 'b' , 'c')
            >>> it(obj).should.have.properties(['a', 'b' , 'c'])
        '''
        propers = []
        for i in args:
            if isinstance(i, list):
                propers.extend(i)
            else:
                propers.append(i)
        for proper in propers:
            self.__property(proper)
        return self

    def own_properties(self, *args):
        '''
        属性列表断言. 必须是实例自己的属性
        Sample:
            >>> it(obj).should.have.properties('a', 'b' , 'c')
            >>> it(obj).should.have.properties(['a', 'b' , 'c'])
        '''
        propers = []
        for i in args:
            if isinstance(i, list):
                propers.extend(i)
            else:
                propers.append(i)
        for proper in propers:
            self.__property(proper, True)
        return self

    def __key(self, name):
        res = name in self._val
        if self._not:
            res = not res
        msg_format = '{0} should{1} have key {2}'.format
        msg = msg_format(self._val, self._flag, name)
        self._assert(res, msg)
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


def it(obj):
    ret = _Should(obj)
    ret.use(Chain)
    return ret

should = it
