# should

[![travis](https://img.shields.io/travis/Ralph-Wang/should.svg?style=flat-square)](https://travis-ci.org/Ralph-Wang/should)
![pypi-downloads](https://img.shields.io/pypi/dm/should.svg?style=flat-square)


```
所谓断言: tj 之前无 should, tj 之后全 should
```

Python 版本的 [should](https://github.com/shouldjs/should.js) 断言库

有借鉴这个 [pyshould](https://github.com/drslump/pyshould)

## TODO

* 原 should 的其它接口
* keys 取反的逻辑需要重新考虑
* 详尽一点的文档


### 既然有了 pyshould, 为什么要重新造轮子?

* an, of, a, and, be, have, with, which 这些应该作为链式调用的属性存在
而不是 `be_integer` 这样的函数前缀

* 不适应 pyshould 中重载运算符的做法

### 借鉴的地方?
~~因为 Python 里的匿名函数没有 JavaScript 中那样强大, 对于 `throw`~~
~~的测试没有采用原 should 的方式, 而选择用 pyshould 中 with 的方式~~

* 借鉴个毛啊, 虽然 Python 的匿名函数不那么强大, 但应付 raise 完全足够了

## 安装:

```
pip install should
```

## 使用方法:


```python
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
```

* 更多例子请参考 [test.py](https://github.com/Ralph-Wang/should/blob/master/test.py)

## 不足:

* 因为 Python 语言特性, 不能对 type 或 object 进行 mixin.
  所以只能使用静态调用的方式. 最前面用 `it` 调用句子通一点了

* Python 中逻辑词 `and`,`not`,`with` 是保留字, 可以作为属性名称存在,
  但直接用点号(.)调用解释器会报语法错误... 所以取反属性用 `no`. 连结词就用
  `also` 代替了.

## License

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
