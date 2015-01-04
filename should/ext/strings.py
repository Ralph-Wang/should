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
        matrix = {
                dict: self.match_dict,
                list: self.match_list,
                str: self.match_string
                }
        t = type(self._val)
        if t not in matrix:  # in case of unicode
            self.match_string(exp)
        else:
            matrix[t](exp)

    def basic_match(self, reg, origin):
        return re.search(reg, origin) is not None

    def match_string(self, exp):
        res = self.basic_match(exp, self._val)
        msg = '{0} should match {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    def match_list(self, exp):
        msg = '{0} in {1} should match {2}'.format
        res = False
        for item in self._val:
            res = self.basic_match(exp, item)
            self._assert(res, msg(item, self._val, exp), reset=False)
        self._reset()

    def match_dict(self, exp):
        msg = '({0},{1}) in {2} should match {3}'.format
        res = False
        for key, value in self._val.items():
            res = self.basic_match(exp, value)
            self._assert(res, msg(key, value, self._val, exp), reset=False)
        self._reset()


    search = match
