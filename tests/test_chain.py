#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it

class Test_Chain(object):

    def test_no(self):
        it(0).be.no.equal(5)
        it(0).be.no.dict
        it(0).be.no.ok
