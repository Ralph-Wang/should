#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_Containers(object):

    def test_empty(self):
        it([]).should.be.empty
        it({}).should.be.empty
        it(()).should.be.empty


        it((1,2,3,)).shouldnt.be.empty
        it([1,2,3,]).shouldnt.be.empty
        it({1:2,3:4}).shouldnt.be.empty

    def test_count(self):
        it([1, 2, 3]).should.count(3, 1)
        it([1, 2, 2]).should.count(2, 2)
        it((1, 2)).should.count(2, 1)
        it((1, 2)).should.no.count(3, 1)
        it({'k1': 1, 'k2': 1}).should.count(1, 2)

    def test_contain(self):
        it([1, 2, 3]).should.contain(1)
        it(set([1, 2, 3])).should.contain(3)
        it({'a': 1, 'b': 2}).should.contain('a')

        it([1, 2, 3]).contain(1, 2)
        it(set([1, 2, 3])).contain(2, 3)
        it({'a': 1, 'b': 2}).should.contain('a', 'b')

    def test_length(self):
        it([]).have.length(0)
        it([1] * 10).have.length(10)
        it('abc').have.length(3)
        it('abcdefg').have.length(7)
        it({}).have.length(0)
        it({'k1': 'v1', 'k2': 'v2'}).have.length(2)

    def test_key(self):
        it({'l1': 'v1'}).have.key('l1').which.should.be.equal('v1')
        it({'l1': 'v1'}).have.no.key('l2').which.be.none

    def test_keys(self):
        it({'l1': 'v1', 'l2': 'v2'}).have.keys('l1', 'l2')
        it({'l1': 'v1', 'l2': 'v2'}).have.keys(['l1', 'l2'])
