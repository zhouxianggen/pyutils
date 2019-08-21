#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyutils',
        version = '1.0',
        install_requires = [], 
        description = 'my python utils',
        url = 'https://github.com/zhouxianggen/pyutils.git', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyutils'],
        data_files = [ ],  
        entry_points = { }   
        )
