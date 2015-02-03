# -*- coding: utf-8 -*-

__all__ = ['ContainerAssertions']


class CommonAssertions(object):

    @property
    def empty(self):
        '''
        断言容器为空
        '''
        self.length(0)
        return self

    def length(self, exp):
        res = len(self._val) == exp
        msg = '{0} should have length {1}'.format
        self._assert(res, msg(self._val, exp))
        return self

    def contain(self, *args):
        for exp in args:
            res = exp in self._val
            msg = '{0} should contain {1}'.format
            self._assert(res, msg(self._val, exp), reset=False)
        self._reset()
        return self

    def count(self, value, num):
        if isinstance(self._val, dict):
            res = (self._val.values().count(value) == num)
        else:
            res = (self._val.count(value) == num)
        msg = '{0} should contain {1} of {2}'.format
        self._assert(res, msg(self._val, num, value))
        return self

class DictAssertions(object):

    def key(self, name):
        '''
        键值断言. 针对字典的键. 会改变链式调用的断言值.
        不存在的 key 会将链式调用值变为 None
        '''
        self.__key(name)
        self._val = self._val.get(name, None)
        return self

    def keys(self, *args):
        '''
        键值列表断言. 针对字典的键
        '''
        keys = []
        for i in args:
            if isinstance(i, list):
                keys.extend(i)
            else:
                keys.append(i)

        for key in keys:
            self.__key(key)
        return self

    def __key(self, name):
        res = name in self._val
        msg_format = '{0} should have key {1}'.format
        msg = msg_format(self._val, name)
        self._assert(res, msg)
        return self


class ContainerAssertions(CommonAssertions, DictAssertions):
    pass
