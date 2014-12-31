# -*- coding: utf-8 -*-

class ValueAssertions(object):

    @property
    def ok(self):
        '''
        boolean 断言, 值的布尔值为 True
        Sample:
            >>> it(1).should.be.ok
            >>> it(0).should.be.no.ok
        '''
        res, msg = self._ok(self._val)
        self._assert(res, msg)
        return self

    def _ok(self, actual):
        res = not bool(actual) if self._not else bool(actual)
        msg_format = '{0}\'s bool value is {1}True'.format
        return res, msg_format(actual, self._flag)

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

