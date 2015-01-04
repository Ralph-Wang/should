# -*- coding: utf-8 -*-

__all__ = ['ValueAssertions']


class ValueAssertions(object):

    def equal(self, exp):
        res = self._val == exp
        msg = '{0} should be equal to {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    @property
    def true(self):
        return self._values(True)

    @property
    def false(self):
        return self._values(False)

    @property
    def none(self):
        return self._values(None)

    def _values(self, value):
        res, msg = self.__values(value, self._val)
        self._assert(res, msg)
        return self

    def __values(self, exp, actual):
        res = actual is exp
        msg_format = '{0} should be {1}'.format
        return res, msg_format(actual, exp)

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
        res = bool(actual)
        msg_format = '{0}\'s bool value should be True'.format
        return res, msg_format(actual)
