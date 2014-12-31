# -*- coding: utf-8 -*-

class _ChainMeta(object):

    def __new__(cls, name, bases, attrs):
        chain = property(lambda self: self)
        names = ['should', 'have', 'an', 'of', 'a', 'be', 'also', 'which']
        attrs.update({}.fromkeys(names, chain))
        return type(name, bases, attrs)


class Chain(object):
    __metaclass__ = _ChainMeta
