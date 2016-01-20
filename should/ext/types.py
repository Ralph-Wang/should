# -*- coding: utf-8 -*-

from functools import partial

__all__ = ['TypeAssertions']


class IsAAssertions(object):

    def subclassof(self, exp):
        res = issubclass(self._val, exp)
        msg = "{0} should be subclass of {1}".format
        self._assert(res, msg(self._val, exp))
        return self

    def instanceof(self, exp):
        res = isinstance(self._val, exp)
        msg = '{0} should be instance of {1}'.format
        self._assert(res, msg(self._val, exp))
        return self


def type_assert(exp, self):
    '''
    exp 会做偏函数, 所以对象会被绑定在第二个参数上
    '''
    actual = type(self._val)
    res = actual is exp
    msg_format = '{0} should be {1}'.format
    self._assert(res, msg_format(actual, exp))
    return self


def type_meta(name, bases, attrs):
    types = list(filter(lambda t: type(t) is type, __builtins__.values()))
    types.remove(property)
    for t in types:
        attrs[t.__name__] = property(partial(type_assert, t))
    return type(name, bases, attrs)

_TypeAssertions = type_meta('_TypeAssertions', (object,), {})


class TypeAssertions(_TypeAssertions, IsAAssertions):
    pass
