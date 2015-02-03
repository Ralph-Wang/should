#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_Properties(object):

    def test_proper(self):
        class A:
            a = 1
        a = A()
        it(a).should.have.proper('a').which.should.be.equal(1)
        it(a).should.have.property('a').which.should.be.equal(1)
        it(a).should.have.no.property('c').which.should.be.none

    def test_own_proper(self):
        class A:
            a = 1

            def __init__(self):
                self.b = 1
        a = A()
        it(a).should.have.no.own_proper('a')
        it(a).should.have.own_proper('b').which.should.be.equal(1)
        it(a).should.have.no.own_property('a')
        it(a).should.have.own_property('b').which.should.be.equal(1)

    def test_properties(self):
        class A:
            a = 1
            b = 2
            c = 1
        a = A()
        it(a).should.have.properties('a', 'b', 'c')
        it(a).should.have.properties(['a', 'b', 'c'])

    def test_own_properties(self):
        class A:

            def __init__(self):
                self.a = 1
                self.b = 2
                self.c = 1
        a = A()
        it(a).should.have.own_properties('a', 'b', 'c')
        it(a).should.have.own_properties(['a', 'b', 'c'])
