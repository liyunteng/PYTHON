#!/usr/bin/env python
# -*- coding: utf-8 -*-

# num.py - num

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 360, 50)
y = np.sin(np.radians(x))

plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x)')
plt.plot(x, y)
plt.show()
