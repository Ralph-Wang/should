# -*- coding: utf-8 -*-

from functools import partial

__all__ = ['TypeAssertions']

def type_assert(exp, self):
    '''
    exp 会做偏函数, 所以对象会被绑定在第二个参数上
    '''
    actual = type(self._val)
    res = (actual is not exp) if self._not else (actual is exp)
    msg_format = '{0} should be {1}{2}'.format
    self._assert(res, msg_format(actual, self._flag, exp))
    return self

def type_meta(name, bases, attrs):
    types = list(filter(lambda t: type(t) is type, __builtins__.values()))
    types.remove(property)
    for t in types:
        attrs[t.__name__] = property(partial(type_assert, t))
    return type(name, bases, attrs)

TypeAssertions = type_meta('TypeAssertions', (object,), {})
