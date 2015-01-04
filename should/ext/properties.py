# -*- coding: utf-8 -*-


class PropertyAssertions(object):

    def proper(self, name):
        self.__property(name, False)
        # 修改链式调用中需要断言的值
        self._val = getattr(self._val, name, None)
        return self

    property = proper

    def own_proper(self, name):
        self.__property(name, True)
        # 修改链式调用中需要断言的值
        self._val = getattr(self._val, name, None)
        return self

    own_property = own_proper

    def __property(self, name, own=False):
        if own:
            pps = self._val.__dict__.keys()
        else:
            pps = dir(self._val)
        res = name in pps
        msg_format = '{0} should{1} have {2}property {3}'.format
        msg = msg_format(self._val, self._flag, 'own ' if own else '', name)
        self._assert(res, msg)
        return self

    def properties(self, *args):
        '''
        属性列表断言. 包含类属性以及继承得到的属性
        Samle:
            >>> it(obj).should.have.properties('a', 'b' , 'c')
            >>> it(obj).should.have.properties(['a', 'b' , 'c'])
        '''
        propers = []
        for i in args:
            if isinstance(i, list):
                propers.extend(i)
            else:
                propers.append(i)
        for proper in propers:
            self.__property(proper)
        return self

    def own_properties(self, *args):
        '''
        属性列表断言. 必须是实例自己的属性
        Sample:
            >>> it(obj).should.have.properties('a', 'b' , 'c')
            >>> it(obj).should.have.properties(['a', 'b' , 'c'])
        '''
        propers = []
        for i in args:
            if isinstance(i, list):
                propers.extend(i)
            else:
                propers.append(i)
        for proper in propers:
            self.__property(proper, True)
        return self
