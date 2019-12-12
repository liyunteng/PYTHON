#!/usr/bin/env python
# -*- coding: utf-8 -*-

# idCheck.py - idCheck

# Date   : 2019/12/12
import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to the Identifier Checker V1.0')
print('Testees must be at least 2 chars long')
inp = input('Identifier to test? ')
if len(inp) > 1:
    if inp[0] not in alphas:
        print('invalid: first symbol must be alphabetic')
    else:
        for i in inp[1:]:
            if i not in alphas + nums:
                print('invalid: remaining symbol must be alphanumeric')
                break
        else:
            print('okay as an identifier')
