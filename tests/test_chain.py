#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_Chain(object):

    def test_no(self):
        it(0).be.no.equal(5)
        it(0).be.no.dict
        it(0).be.no.ok

    def test_chain(self):
        v = it(0)
        it(v).should.be.same(v.should)
        it(v).should.be.same(v.have)
        it(v).should.be.same(v.an)
        it(v).should.be.same(v.of)
        it(v).should.be.same(v.a)
        it(v).should.be.same(v.be)
        it(v).should.be.same(v.also)
        it(v).should.be.same(v.which)
