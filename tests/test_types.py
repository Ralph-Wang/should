#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_Types(object):

    def test_type(self):
        it(0).be.int
        it(True).be.bool
        it('string').be.str
        it([]).be.list
        it(()).be.tuple
        it({}).be.dict

    def test_subclassof(self):
        class A(object):
            pass
        class B(A):
            pass
        class C(B):
            pass

        it(B).should.be.subclassof(A)
        it(C).should.be.subclassof(A)
        it(C).should.be.subclassof(B)
        it(A).shouldnt.be.subclassof(C)

    def test_instanceof(self):
        class A(object):
            pass

        class B(A):
            pass
        a = A()
        b = B()
        it(a).should.be.instanceof(A)
        it(a).should.be.no.instanceof(B)
        it(b).should.be.instanceof(A)
        it(b).should.be.instanceof(B)
