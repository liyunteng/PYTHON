#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hist.py - hist

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt

a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title('histogram')
# plt.savefig('hist.png')
plt.show()
