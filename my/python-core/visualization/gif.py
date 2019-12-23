#!/usr/bin/env python
# -*- coding: utf-8 -*-

# git.py - git

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
line, = axes1.plot(np.random.rand(10))


def update(data):
    line.set_ydata(data)
    return line


def data_gen():
    while True:
        yield np.random.rand(10)


ani = animation.FuncAnimation(fig, update, data_gen, interval=2*1000)
plt.show()
