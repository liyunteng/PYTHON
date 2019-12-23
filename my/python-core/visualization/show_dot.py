#!/usr/bin/env python
# -*- coding: utf-8 -*-

# show_dot.py - show_dot

# Date   : 2019/12/23
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(0, 2*np.pi, 128)
y = np.sin(x)
ln = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')


def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln


def gen_dot():
    for i in np.linspace(0, 2*np.pi, 128):
        newdot = [i, np.sin(i)]
        yield newdot


def update(data):
    dot.set_data(data[0], data[1])
    return dot,


ani = animation.FuncAnimation(fig, update, frames=gen_dot,
                              interval=100, init_func=init)
# ani.save('show_dot.gif', writer='imagemagick', fps=30)
plt.show()
