#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sincos.py - sincos

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(1, 2, 1)
plt.plot(x, y_sin)
plt.title('sin')
plt.subplot(1, 2, 2)
plt.plot(x, y_cos)
plt.title('cos')
plt.show()
