# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.4.0'

setup(name='should',
      version=version,
      description="assert with should",
      long_description="""
      不太会 RST, 详情及源码见 https://github.com/Ralph-Wang/should

      from should import it

      it(1).should.be.int.also.be.equal(1)

      it(lambda: int('abc')).should.throw(ValueError)
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
