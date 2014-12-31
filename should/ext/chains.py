# -*- coding: utf-8 -*-


def chain_meta(name, bases, attrs):
    chain = property(lambda self: self)
    names = ['should', 'have', 'an', 'of', 'a', 'be', 'also', 'which']
    attrs.update({}.fromkeys(names, chain))
    return type(name, bases, attrs)


Chain = chain_meta('Chain', (object,), {})
