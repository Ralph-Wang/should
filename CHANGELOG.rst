Change Log
----------------

v0.5.1
~~~~~~~~~~~~~~~~

* 小重构, 删除 _flag 属性

v0.5.1
~~~~~~~~~~~~~~~~

* 修复 #1, 解决自测问题
* 结构化目录, 让代码清晰一点
* 链式调用部分用元类改写
* less/greater 添加 'below/above' 别名


v0.5.0
~~~~~~~~~~~~~~~~

* 删除原 `raises` 接口, 不再支持 with should.raises 语法
* `raises` 接口改为 `throw` 的等价接口
* `key` 会改变链式调用. 后续值为键所对应的值

v0.4.8
~~~~~~~~~~~~~~~~

* fix `throw` 在 2.* 只能接受 `str` 的问题
* 如 it(1).should.be.int 的类型断言, 不断言 property
* proper 和 own_proper 增加别名 property 和 own_property
* 增加 properties 和 own_properties. 对对象支持列表式断言
* 增加 keys, 对字典支持列表式断言

v0.4.7
~~~~~~~~~~~~~~~~

* 添加 `within` 接口
* should.py 文件中添加自文档
* 添加 `proper` / `own_proper` 接口

v0.4.6
~~~~~~~~~~~~~~~~

* fix #2. match 不支持多行
* 添加 `search` 接口, 与 `match` 等价, 但更贴近 Python re 的接口

v0.4.5
~~~~~~~~~~~~~~~~

* 增加 `match` 接口, 进行正则匹配断言
* 增加 `empty` 属性, 直接判断容器或序列是否为空
* 只有连接词, be, have 会出现在 Assertion Error 中
* `throw` 接口支持断言 throw 信息

v0.4.4
~~~~~~~~~~~~~~~~

* 安装失败修复

v0.4.3
~~~~~~~~~~~~~~~~

* 类型断言如 `it(1).should.be.int` 支持所有内建类型
* 添加 `instanceof` 断言, 支持其它类型或弱类型断言
* 链式调用 'be'/'have' 时, Error 信息正确显示 have 和 be
