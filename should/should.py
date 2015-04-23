# -*- coding: utf-8 -*-

'''
should.py:
    BDD assertion library

    Sample:
        >>> from should import it
        >>> it(1).should.be.int.also.be.equal(1)
        >>> it(lambda: foo()).should.throw(ValueError)
        >>> it(lambda: foo()).should.throw("Some Message")
'''

import sys

PY3 = sys.version_info[0] == 3

if not PY3:
    reload(sys)
    sys.setdefaultencoding('utf8')


class Should(object):

    def __init__(self, val=None):
        self._val = val
        self._not = False  # `not` flag

    @property
    def no(self):
        '''断言取反'''
        self._not = True
        return self

    shouldnt = no

    def _reset(self):
        self._not = False
        return self

    def _assert(self, res, msg, reset=True):
        ''' 统一的 assert 方法, 每次断言之后取消取否 '''
        if self._not:
            res = not res
            msg = msg.replace('should', 'should not')
        assert res, msg
        if reset:
            self._reset()
        return self

    def use(self, cls):
        origin = self.__class__
        self.__class__ = type('shouldobj', (cls, origin), {})
        return self
