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

from .should import Should
from .ext import *


def it(obj):
    ret = Should(obj)
    ret.use(Chain)\
        .use(ValueAssertions)\
        .use(ErrorAssertions)\
        .use(PropertyAssertions)
    return ret

should = it
