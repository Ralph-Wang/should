Change Log
----------------

v0.4.5
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
