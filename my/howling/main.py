#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main.py - main

# Date   : 2020/12/16
import numpy as np
import numpy.fft as nf
from scipy.io import wavfile
import matplotlib.pyplot as plt


def read_wav(file_path):
    framerate,data = wavfile.read(file_path)
    nframes = len(data)
    nchannels = 1
    # data = data / np.max(data)
    # data = np.reshape(data, [nframes, nchannels])
    print('framerate: {}\nnchannels: {}\nnframes: {}\n'.format(
        framerate, nchannels, nframes))
    t = np.arange(0, nframes) * (1.0 / framerate)
    print('time({}s): {}'.format(1.0 / 8000 * len(t), t))
    print('data: {}\n'.format(data))
    return(t, data)

def trans(t, data):
    freqs = np.abs(nf.fftfreq(t.size, t[1]-t[0]))
    complex_array = nf.fft(data)
    pows = np.abs(complex_array)

    found_freq = freqs[pows.argmax()]
    data_indices = np.where(np.abs(pows) > np.abs(0.4e7))
    filter_complex_array = complex_array.copy()
    filter_complex_array[data_indices] = 0
    filter_pows = np.abs(filter_complex_array)
    filter_data = nf.ifft(filter_complex_array).real
    return(t, filter_data)

def show1(t, data):
    data = nf.fft(data) / len(data)

    V = []
    print('data len: {}'.format(len(data)))
    for x in range(0, len(data)):
        if x == 0:
            V.append(data[x])
        else:
            V.append((data[x] - data[x-1]))

    N = 10
    weight = np.ones(N)/N
    A = np.convolve(V, weight, mode='same')

    S = []
    for x in range(0,len(A)):
        S.append(np.std(A[x+1-N:x+1]))

    THRESHOLD = 0.15
    for x in range(0, len(S)):
        if S[x] < THRESHOLD and True:
            data[x] = 0

    # for x in range(0, len(data)):
    #     f = np.abs(x * 8000.0 / len(data))
    #     if (f >= 1000.0 and f <= 2000.0) or (f >= 5000.0 and f <= 6000.0):
    #         data[x] = 0.0

    print(A)
    # print(S)

    print('A max: {}'.format(A.max()))
    print('A len: {}'.format(len(A)))
    print('S max: {}'.format(max(S)))
    print('S len: {}'.format(len(S)))

    sample = np.arange(0, len(data))
    freqs = nf.fftfreq(t.size, t[1] - t[0])

    plt.figure('abc')
    plt.subplot(411)
    plt.xlabel('sample')
    plt.ylabel('V(f)')
    plt.grid(linestyle=':')
    plt.plot(sample, V)

    plt.subplot(412)
    plt.xlabel('sample')
    plt.ylabel('A(f)')
    plt.grid(linestyle=':')
    plt.plot(sample, A)

    plt.subplot(413)
    plt.xlabel('sample')
    plt.ylabel('STD(f)')
    plt.grid(linestyle=':')
    plt.plot(freqs, S)

    plt.subplot(414)
    plt.xlabel('Freq')
    plt.ylabel('Power')
    plt.plot(freqs, data)

    data = nf.ifft(data) * len(data)
    wavfile.write('/Users/lyt/out.wav', 8000, np.int16(data))
    return (t, data)


def show2(t1, data1, t2, data2):
    plt.figure('Filter')
    plt.subplot(231)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Signal', fontsize=12)
    plt.grid(linestyle=':')
    plt.plot(t1, data1, c='orangered', label='audio')

    freqs = nf.fftfreq(t1.size, t1[1]-t1[0])
    complex_array = nf.fft(data1)
    pows = complex_array
    plt.subplot(232)
    plt.xlabel('Freq', fontsize=12)
    plt.ylabel('Power', fontsize=12)
    plt.grid(linestyle=':')
    plt.plot(freqs, pows, c='limegreen', label='audio')

    plt.subplot(233)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Freq', fontsize=12)
    plt.grid(linestyle=':')
    plt.specgram(data1, Fs=8000, scale_by_freq=True, sides='default')


    freqs = nf.fftfreq(t2.size, t2[1]-t2[0])
    complex_array = nf.fft(data2)
    pows = complex_array

    plt.subplot(234)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Signal', fontsize=12)
    plt.grid(linestyle=':')
    plt.plot(t2, data2, c='orangered', label='filter')

    plt.subplot(235)
    plt.xlabel('Freq', fontsize=12)
    plt.ylabel('Power', fontsize=12)
    plt.grid(linestyle=':')
    plt.plot(freqs, pows, c='limegreen', label='fiter')

    plt.subplot(236)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Freq', fontsize=12)
    plt.grid(linestyle=':')
    plt.specgram(data2, Fs=8000, scale_by_freq=True, sides='default')

    # wavfile.write('/Users/lyt/filter.wav', 8000, np.int16(data2))
    plt.show()

def main():
    # t1, data1  = read_wav('/Users/lyt/ok.wav')
    t1, data1  = read_wav('/Users/lyt/abc.wav')
    t3, data3 = show1(t1, data1)
    # show2(t1, data1, t3, data3)
    show2(t1, data1, t3, data3)

if __name__ == '__main__':
    main()
