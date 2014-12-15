#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import should


class Test_Should(object):
    def test_type(self):
        should(0).be.int
        should(True).be.bool
        should('string').be.str
        should([]).be.list
        should(()).be.tuple
        should({}).be.dict

    def test_uniq_values(self):
        should(None).be.none
        should(True).be.true
        should(False).be.false
        should(1).be.no.none
        should(1).be.no.true
        should(1).be.no.false

    def test_ok(self):
        should(1).be.ok
        should([1]).be.ok
        should((1,)).be.ok
        should({'key': 'value'}).be.ok
        # 没有 __nozero__(2.*) or __bool__(3.*)
        class A:
            pass
        should(A()).be.ok

    def test_equal(self):
        should(0).be.equal(0)
        should('string').be.equal('string')
        should({}).be.equal({})
        should([]).be.equal([])
        should(()).be.equal(())

        # 自定义的等于
        class A(object):
            def __init__(self, val):
                self.val = val
            def __eq__(self, other):
                return self.val != other.val
        should(A(1)).be.equal(A(3))

    def test_startswith(self):
        should('abcdefg').be.startswith('abc')
        should('abc').be.no.startswith('.git')

    def test_endswith(self):
        should('abcdefg').be.endswith('efg')
        should('abc').be.no.endswith('.git')

    def test_no(self):
        should(0).be.no.equal(5)
        should(0).be.no.dict
        should(0).be.no.ok

    def test_less(self):
        should(0).be.less(5)
        should(5).be.no.less(5)
        should(5).be.no.less(4)

    def test_greater(self):
        should(0).be.greater(-1)
        should(0).be.no.greater(0)
        should(0).be.no.greater(5)

    def test_contain(self):
        should([1,2,3]).contain(1)
        should(set([1,2,3])).contain(3)

    def test_length(self):
        should([]).have.length(0)
        should([1] * 10).have.length(10)
        should('abc').have.length(3)
        should('abcdefg').have.length(7)
        should({}).have.length(0)
        should({'k1': 'v1', 'k2': 'v2'}).have.length(2)

    def test_key(self):
        should({'l1': 'v1'}).have.key('l1')
        should({'l1': 'v1'}).have.no.key('l2')

    def test_raises(self):
        with should.raises(IndexError):
            a = []
            a[0]

        with should.raises(ValueError):
            int('abc')

        try:
            with should.raises(ValueError):
                int('13')
        except AssertionError:
            pass

    def test_msg(self):
        try:
            should(1).be.equal(2)
        except AssertionError as e:
            assert 'not' in str(e)

        try:
            should(1).be.no.equal(1)
        except AssertionError as e:
            assert 'not' not in str(e)
