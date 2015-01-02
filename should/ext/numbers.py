# -*- coding: utf-8 -*-


__all__ = ['NumberAssertions']




class NumberAssertions(object):
    def less(self, exp):
        res = self._val < exp
        if self._not:
            res = not res
        msg = '{0} should {1}be less than {2}'.format
        self._assert(res, msg(self._val, self._flag, exp))
        return self

    below = less

    def greater(self, exp):
        res = self._val > exp
        if self._not:
            res = not res
        msg = '{0} should {1}be greater than {2}'.format
        self._assert(res, msg(self._val, self._flag, exp))
        return self

    above = greater

    def within(self, less, greater):
        '''
        范围断言, 值在 less, greater 之间
        '''
        res = less <= self._val <= greater
        msg_format = '{0} should be {1}within {2}, {3}'.format
        if self._not:
            res = not res
        msg = msg_format(self._val, self._flag, less, greater)
        self._assert(res, msg)
        return self
