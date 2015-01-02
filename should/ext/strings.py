# -*- coding: utf-8 -*-

import re

__all__ = ['StringAssertions']

class StringAssertions(object):
    def startswith(self, exp):
        res = self._val.startswith(exp)
        if self._not:
            res = not res
        msg = '{0} should {1}startswith {2}'.format
        self._assert(res, msg(self._val, self._flag, exp))
        return self

    def endswith(self, exp):
        res = self._val.endswith(exp)
        if self._not:
            res = not res
        msg = '{0} should {1}endswith {2}'.format
        self._assert(res, msg(self._val, self._flag, exp))
        return self

    def match(self, exp):
        res = re.search(exp, self._val) is not None
        if self._not:
            res = not res
        msg = '{0} should {1}match {2}'.format
        self._assert(res, msg(self._val, self._flag, exp))
        return self

    search = match
