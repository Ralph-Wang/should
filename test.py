#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_it(object):
    def test_type(self):
        it(0).be.int
        it(True).be.bool
        it('string').be.str
        it([]).be.list
        it(()).be.tuple
        it({}).be.dict

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

    def test_startswith(self):
        it('abcdefg').be.startswith('abc')
        it('abc').be.no.startswith('.git')

    def test_endswith(self):
        it('abcdefg').be.endswith('efg')
        it('abc').be.no.endswith('.git')

    def test_no(self):
        it(0).be.no.equal(5)
        it(0).be.no.dict
        it(0).be.no.ok

    def test_less(self):
        it(0).be.less(5)
        it(5).be.no.less(5)
        it(5).be.no.less(4)

    def test_greater(self):
        it(0).be.greater(-1)
        it(0).be.no.greater(0)
        it(0).be.no.greater(5)

    def test_within(self):
        it(0).should.be.within(-1,1)
        it(10).should.be.within(8, 10)
        it(20).should.be.no.within(8, 10)

    def test_contain(self):
        it([1,2,3]).contain(1)
        it(set([1,2,3])).contain(3)

    def test_proper(self):
        class A:
            a = 1
        a = A()
        it(a).should.have.proper('a').which.should.be.equal(1)
        it(a).should.have.property('a').which.should.be.equal(1)

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


    def test_length(self):
        it([]).have.length(0)
        it([1] * 10).have.length(10)
        it('abc').have.length(3)
        it('abcdefg').have.length(7)
        it({}).have.length(0)
        it({'k1': 'v1', 'k2': 'v2'}).have.length(2)

    def test_key(self):
        it({'l1': 'v1'}).have.key('l1')
        it({'l1': 'v1'}).have.no.key('l2')

    def test_keys(self):
        it({'l1': 'v1', 'l2': 'v2'}).have.keys('l1', 'l2')
        it({'l1': 'v1', 'l2': 'v2'}).have.keys(['l1', 'l2'])

    def test_instanceof(self):
        it({'l1': 'v1'}).should.be.instanceof(dict)
        it({'l1': 'v1'}).should.be.no.instanceof(int)
        class A:
            pass
        it(A()).should.be.instanceof(A)

    def test_search(self):
        it('abcdefg').should.search(r'.')
        it('test@163.com').should.search(r'(\w|_)+@(\w|_)+?\.(\w|_)+')
        it('aaa').should.no.search(r'bbb')
        it('abc\ndef').should.search(r'def')

    def test_match(self):
        it('abcdefg').should.match(r'.')
        it('test@163.com').should.match(r'(\w|_)+@(\w|_)+?\.(\w|_)+')
        it('aaa').should.no.match(r'bbb')
        it('abc\ndef').should.match(r'def')

    def test_empty(self):
        it('').should.be.empty
        it([]).should.be.empty
        it(()).should.be.empty
        it({}).should.be.empty
        it(set()).should.be.empty

        it('1').should.be.no.empty
        it([1]).should.be.no.empty
        it((1,)).should.be.no.empty
        it({1: 2}).should.be.no.empty
        it(set([1])).should.be.no.empty

    def test_raises(self):
        with it.raises(IndexError):
            a = []
            a[0]

        with it.raises(ValueError):
            int('abc')

        try:
            with it.raises(ValueError):
                int('13')
        except AssertionError:
            pass

    def test_throw(self):
        it(lambda: int('abc')).throw(ValueError)
        it(lambda: int('123')).no.throw(ValueError)

    def test_throw_msg(self):
        def foo():
            raise ValueError("some msg")

        # 3.2 没有 u'' 字面量... 能不这么奇葩么...
        # it(foo).should.throw(ValueError).also.throw(u"some msg")
        it(foo).should.throw(ValueError).also.throw("some msg")

        it(foo).should.no.throw("123")

    def test_msg(self):
        try:
            it(1).be.equal(2)
        except AssertionError as e:
            assert 'not' not in str(e)
            assert 'be' in str(e)

        try:
            it([1]).should.contain(2)
        except AssertionError as e:
            assert 'not' not in str(e)
            assert 'be' not in str(e)

        try:
            it(1).be.no.equal(1)
        except AssertionError as e:
            assert 'not' in str(e)
            assert 'be' in str(e)

        try:
            it({'k1': 'v1'}).should.have.key('l1')
        except AssertionError as e:
            assert 'have' in str(e)
            assert 'be' not in str(e)
