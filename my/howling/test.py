#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test.py - test

# Date   : 2020/12/17
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 8000
fft_size = 512

t = np.arange(0, 1.0, 1.0/sampling_rate)
x = np.sin(2*np.pi*156.25*t) + 2*np.sin(2*np.pi*234.375*t)
xs = x[:fft_size]
xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

plt.figure(figsize=(8,4))
plt.subplot(211)
plt.xlabel("time (second)")
plt.plot(t[:fft_size], xs)

plt.subplot(212)
plt.xlabel('Freq')
plt.plot(freqs, xfp)
plt.show()
