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

    def _assert(self, res, msg):
        ''' 统一的 assert 方法, 每次断言之后取消取否 '''
        assert res, msg
        self._not = False

    @property
    def _flag(self):
        return 'not ' if self._not else ''

    def use(self, cls):
        origin = self.__class__
        self.__class__ = type('shouldobj', (cls, origin), {})
        return self
