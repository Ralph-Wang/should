# should

[![travis](https://img.shields.io/travis/Ralph-Wang/should.svg?style=flat-square)](https://travis-ci.org/Ralph-Wang/should)
[![Coverage Status](https://img.shields.io/coveralls/Ralph-Wang/should.svg?style=flat-square)](https://coveralls.io/r/Ralph-Wang/should)
[![pypi-version](https://img.shields.io/pypi/v/should.svg?style=flat-square)](https://pypi.python.org/pypi/should)
![pypi-downloads](https://img.shields.io/pypi/dm/should.svg?style=flat-square)


```
所谓断言: tj 之前无 should, tj 之后全 should
```

Python 版本的 [should](https://github.com/shouldjs/should.js) 断言库

有借鉴这个 [pyshould](https://github.com/drslump/pyshould)

## TODO

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


# lambda 版异常断言
it(lambda: int('abc')).should.throw(ValueError)
it(lambda: int('123')).should.no.throw(ValueError)
```

## 接口说明:


### 调用链

下面这些属性对断言没有任何影响, 只作为链式调用的中间属性
`should`, `have`, `an`, `of`, `a`, `be`: `be`, `also`, `which`

### .no

`.no` 对当前断言取反.
Python 中, `not` 是保留字, 不能使用. 所以选择 `.no`


### .ok

断言对象的布尔值为真 (`bool(obj)`)

```python
it(1).should.be.ok
it(True).should.be.ok
it([]).should.be.no.ok
```

### .true / .false / .none

断言对象就是 True, False, None (`is`)

因为大写开头的 True/False/None 在 3.\* 中变成保留字, 所以这里改用小写

```python
it(True).should.be.true
it(False).should.be.false
it(None).should.be.none
```

### .equal(value) ###

断言对象是否与 *value* 相等 (`==`)

```python
it(1).should.be.equal(1)
it([]).should.be.equal([])
it(list(range(1,4))).should.be.equal([1,2,3])
```


### .startswith(substr) / .endswith(substr) ###

断言字符串是否以 *substr* 开头/结尾 (`str.startswitdh`/`endswith`)

```python
it('Hello World!').should.startswith('He')
it('WTF GFW').should.endswith('GFW')
```

### .within(from, to) ###

断言对象值在 *from* 和 *to* 之间 (from <= val <= to)

```python
it(1).should.be.within(0, 5)
```

### .less(value) / .greater(value) ###

断言对象值小于(<)或大于(>) *value*

```python
it(9).should.be.less(11)
it(25).should.be.greater(22)
```

### .same(obj) ###

与 obj 是同一个对象 (`is`)

```
class A():
   pass

a = b = A()
it(a).should.be.same(b)
```

### 类型断言 ###

除 `<type 'property'>` 以外的内建类型断言 (`is`)

```python
it(1).should.be.int
it([]).should.be.list
```

### .isinstanceof(type) ###

断言对象是 `type` 的实例 (`isinstance`)

```python
class A(int):
    pass
it(A(1)).should.be.no.int
it(A(1)).should.be.instanceof(int)
```

### .count(value, num)

断言容器中包含 num 个 value 值 (`[].count(value) == num`)
支持字典 (`{}.values().count(value) == num`)

```python
it([1,2,3]).should.count(3, 1)
it((1,2,2)).should.count(2, 2)
it({'k1': 1, 'k2': 1}).should.count(1, 2)
```

### .contain(item1, item2...)

断言对象包含所有元素 (`itemN in val`)

```python
it([1, 2, 3]).should.contain(1)
it(set([1, 2, 3])).should.contain(2, 3)
it({'a': 1, 'b': 2}).should.contain('a')
```

### .property(name) ###

断言对象有属性 `name`. (in dir(obj)).
`.property` 接口后调用链中对断言对象变更为对应属性的值

```python
class A:
    a = 1
it(A()).should.have.property('a').which.should.be.equal(1)
```

### .own_property ###

断言对象自己有属性 `name`. (in obj.\_\_dict\_\_)
`.own_property` 接口后调用链中对断言对象变更为对应属性的值

```python
class A:
    a = 1
    def __init__(self):
        self.b = 1
it(A()).should.have.no.own_property('a')
it(A()).should.have.no.own_property('b').which.should.be.equal(1)
```

### .properties(name1, name2, ...) / .own_properties(name1, name2, ...) ###

断言对象有一组属性.

这两个接口不会改变调用链

```python
class A:
    a = b = c = 1
    def __init__(self):
        self.d = slef.e = 3
it(A()).should.have.properties('a', 'b', 'c')
it(A()).should.have.own_properties('d', 'e')
```

### .length(value) ###

断言一个 sequence 长度为 `value` (`len`)

```python
it([]).should.have.length(0)
it([1,2,3]).should.have.length(3)
```

### .empty ###

断言一个 sequence 是否为空 (`len(val) == 0`)

```python
it([]).should.be.empty
it([1,2,3]).should.be.no.empty
```

### .key(name) ###

断言一个字典有 `name` 键 (in dict.keys())

`.key` 会改变调用链为该键对应的值

```python
it({'a': 1}).should.have.key('a').which.should.be.equal(1)
```

### .keys(name1, name2, ...) ###

断言对象有一组键.

这两个接口不会改变调用链

```python
it({'a': 1}).should.have.key('a').which.should.be.equal(1)
```

### .match(re_string) / .search(re_string) ###

断言字符串匹配正则 `re_string` (re.search(re_string, **))

```python
it('abc').should.match(r'.c')

lst = ['ww@ww.com', 'test@test.cn', 'cc@bb.net']
it(lst).should.match(r'(\w|_)+@(\w|_)+?\.(\w|_)+')

dct = {'u1': 'www', 'u2': 'bbc'}
it(dct).should.match(r'^\w+')
```

### .throw(Error/msg) ###

断言函数是否抛出异常 `Error` 或 异常信息 `msg`

```python
def foo():
    raise ValueError('some msg')
it(lambda: foo()).should.throw(ValueError)
it(lambda: foo()).should.throw('some msg')
it(lambda: foo()).should.raises(ValueError)
it(lambda: foo()).should.raises('some msg')
```


* 更多例子请参考 [test.py](https://github.com/Ralph-Wang/should/blob/master/tests)

## 不足:

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
