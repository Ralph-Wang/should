#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it
import sys

py3 = sys.version_info[0] == 3


class Test_Errors(object):

    def test_throw(self):
        it(lambda: int('abc')).throw(ValueError)
        it(lambda: int('123')).no.throw(ValueError)

        it(lambda: int('abc')).raises(ValueError)
        it(lambda: int('123')).no.raises(ValueError)

    def test_throw_msg(self):
        def foo():
            raise ValueError("some msg")

        if not py3:
            it(foo).should.throw(ValueError).also.throw(u"some msg")
        it(foo).should.throw(ValueError).also.throw("some msg")
        it(foo).should.raises(ValueError).also.raises("some msg")

        it(foo).should.no.throw("123")
        it(foo).should.no.raises("123")

    def test_embeded(self):
        it(lambda: it(1).should.equal(2)).throw(AssertionError)
