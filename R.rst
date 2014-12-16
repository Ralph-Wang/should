should
==========

.. travis-badge:: https://img.shields.io/travis/Ralph-Wang/should.svg?style=flat-square
    :https://travis-ci.org/Ralph-Wang/should
.. Coverage:: https://img.shields.io/coveralls/Ralph-Wang/should.svg?style=flat-square
    :cover: https://coveralls.io/r/Ralph-Wang/should
.. pypi-version:: https://img.shields.io/pypi/v/should.svg?style=flat-square
.. pypi-downloads:: https://img.shields.io/pypi/dm/should.svg?style=flat-square


::
    所谓断言: tj 之前无 should, tj 之后全 should


安装:
====

Install::
    pip install should


使用方法:
====


Usage Sample::
    from should import it

    # 一般的断言
    it(1).should.be.int
    it({}).should.be.no.ok
    it(2).should.be.equal(2)
    it(10).should.be.no.equal(8)
    it([1,2,3]).should.contain(3)

    # with 版异常断言, 不支持 no, 在 0.5 版本会被删除
    with should.raises(ValueError):
        int('abc')

    # lambda 版异常断言
    it(lambda: int('abc')).should.throw(ValueError)
    it(lambda: int('123')).should.no.throw(ValueError)

- 更多例子请参考
.. test.py:https://github.com/Ralph-Wang/should/blob/master/test.py


License
====

The MIT License

Copyright (c) 2014 Ralph-Wang

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
