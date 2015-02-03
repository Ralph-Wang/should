#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should import it


class Test_Number(object):

    def test_less(self):
        it(0).be.less(5)
        it(5).be.no.less(5)
        it(5).be.no.less(4)

        # below
        it(0).be.below(5)
        it(5).be.no.below(5)
        it(5).be.no.below(4)

    def test_greater(self):
        it(0).be.greater(-1)
        it(0).be.no.greater(0)
        it(0).be.no.greater(5)

        # above
        it(0).be.above(-1)
        it(0).be.no.above(0)
        it(0).be.no.above(5)

    def test_within(self):
        it(0).should.be.within(-1, 1)
        it(10).should.be.within(8, 10)
        it(20).should.be.no.within(8, 10)
