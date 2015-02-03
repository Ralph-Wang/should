#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it
import sys

py3 = sys.version_info[0] == 3


class Test_it(object):
    def test_startswith(self):
        it('abcdefg').be.startswith('abc')
        it('abc').be.no.startswith('.git')

    def test_endswith(self):
        it('abcdefg').be.endswith('efg')
        it('abc').be.no.endswith('.git')


    def test_match(self):
        it('abcdefg').should.match(r'.')
        it(u'test@163.com').should.match(r'(\w|_)+@(\w|_)+?\.(\w|_)+')
        it('aaa').should.no.match(r'bbb')
        it('abc\ndef').should.match(r'def')

    def test_match_list(self):
        case = ['ww@ww.com', 'test@test.cn', 'cc@bb.net']
        it(case).should.match(r'(\w|_)+@(\w|_)+?\.(\w|_)+')
        it(case).should.no.match(r'\d')

    def test_match_dict(self):
        case = {'u1': 'www', 'u2': 'bbc'}
        it(case).should.match(r'^\w+')
        it(case).should.no.match(r'\d')

