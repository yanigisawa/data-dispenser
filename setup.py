#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='data_dispenser',
    version='0.1.0',
    description='Loads data from various formats',
    long_description=readme + '\n\n' + history,
    author='Catherine Devlin',
    author_email='catherine.devlin@gmail.com',
    url='https://github.com/catherinedevlin/data_dispenser',
    packages=[
        'data_dispenser',
    ],
    package_dir={'data_dispenser': 'data_dispenser'},
    include_package_data=True,
    install_requires=[
    ],
    extras_require = {
        'Mongo': ['pymongo',],
        'yaml': ['pyyaml',],
        },
    license="MIT",
    zip_safe=False,
    keywords='data_dispenser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)