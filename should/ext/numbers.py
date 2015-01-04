# -*- coding: utf-8 -*-


__all__ = ['NumberAssertions']


class NumberAssertions(object):

    def less(self, exp):
        res = self._val < exp
        msg = '{0} should be less than {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    below = less

    def greater(self, exp):
        res = self._val > exp
        msg = '{0} should be greater than {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    above = greater

    def within(self, less, greater):
        '''
        范围断言, 值在 less, greater 之间
        '''
        res = less <= self._val <= greater
        msg_format = '{0} should be within {1}, {2}'.format
        msg = msg_format(self._val, less, greater)
        self._assert(res, msg)
        return self
