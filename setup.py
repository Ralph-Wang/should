# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    content = open('R.rst').read() + '\n\n' + open('CHANGELOG.rst').read()
except:
    content = ''

version = '0.4.5'

setup(name='should',
      version=version,
      description="assert with should",
      long_description=content,
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
