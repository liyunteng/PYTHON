#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test1.py - test1

# Date   : 2019/12/23
import matplotlib.pyplot as plt

height = [161, 170, 182, 175, 173, 165]
weight = [50, 58, 80, 70, 59, 55]

plt.scatter(height, weight, alpha=0.7)
plt.xlabel('height')
plt.ylabel('weight')
plt.title('scatter demo')
plt.show()
