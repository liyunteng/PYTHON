#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setup.py - setup

# Date   : 2019/12/21
# python setup.py install
from distutils.core import setup, Extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=['Extest.c'])])
