#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it
import sys

py3 = sys.version_info[0] == 3


class Test_Values(object):

    def test_same(self):
        class A(object):
            pass
        a = A()
        b = A()
        it(a).should.be.same(a)
        it(a).should.be.no.same(b)

    def test_uniq_values(self):
        it(None).be.none
        it(True).be.true
        it(False).be.false
        it(1).be.no.none
        it(1).be.no.true
        it(1).be.no.false

    def test_ok(self):
        it(1).be.ok
        it([1]).be.ok
        it((1,)).be.ok
        it({'key': 'value'}).be.ok
        # 没有 __nozero__(2.*) or __bool__(3.*)

        class A:
            pass
        it(A()).be.ok

    def test_equal(self):
        it(0).be.equal(0)
        it('string').be.equal('string')
        if not py3:
            it(u'string').be.equal(u'string')
            it(u'中文').be.equal(u'中文')
        it({}).be.equal({})
        it([]).be.equal([])
        it(()).be.equal(())

        # 自定义的等于
        class A(object):

            def __init__(self, val):
                self.val = val

            def __eq__(self, other):
                return self.val != other.val
        it(A(1)).be.equal(A(3))
