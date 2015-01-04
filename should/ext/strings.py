# -*- coding: utf-8 -*-

import re

__all__ = ['StringAssertions']


class StringAssertions(object):

    def startswith(self, exp):
        res = self._val.startswith(exp)
        msg = '{0} should startswith {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    def endswith(self, exp):
        res = self._val.endswith(exp)
        msg = '{0} should endswith {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    def match(self, exp):
        res = re.search(exp, self._val) is not None
        msg = '{0} should match {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    search = match
