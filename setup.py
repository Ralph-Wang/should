# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.4.4'

setup(name='should',
      version=version,
      description="assert with should",
      long_description="""
should
----------------

.. image:: https://img.shields.io/travis/Ralph-Wang/should.svg?style-flat-square
    :target: https://travis-ci.org/Ralph-Wang/should
.. image:: https://img.shields.io/coveralls/Ralph-Wang/should.svg?style-flat-square
    :target: https://coveralls.io/r/Ralph-Wang/should

安装:
----------------

::

    pip install should


使用方法:
----------------


::

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


- 更多例子请参考 test.py_

.. _test.py: https://github.com/Ralph-Wang/should/blob/master/test.py


License
----------------

The MIT License
      """,
      keywords='assert,should,test,BDD',
      author='Ralph-Wang',
      author_email='ralph.wang1024@gmail.com',
      url='https://github.com/Ralph-Wang/should',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      py_modules=['should'],
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
