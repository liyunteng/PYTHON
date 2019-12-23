#!/usr/bin/env python
# -*- coding: utf-8 -*-

# draw_sin.py - draw_sin

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-')


def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln


def update(data):
    xdata.append(data)
    ydata.append(np.sin(data))
    ln.set_data(xdata, ydata)
    return ln


ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, interval=1)
print(np.linspace(0, 2*np.pi, 128))
plt.show()
