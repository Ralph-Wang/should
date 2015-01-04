# -*- coding: utf-8 -*-


class ErrorAssertions(object):

    def throw(self, exception):
        '''
        异常断言.
        Sample:
            >>> it(lambda: foo()).should.throw(ValueError)
            >>> it(lambda: foo()).should.throw("Error Message")
        '''
        if str(exception) == exception:
            exe_msg = exception
            exception = Exception
            msg = 'should raise msg:' + exe_msg
        else:
            exe_msg = None
            msg = 'should raise ' + exception.__name__

        try:
            self._val()
        except exception as e:
            res = True
            if exe_msg is not None:
                res = exe_msg in str(e)
        else:
            res = False
        self._assert(res, msg)
        return self

    raises = throw
