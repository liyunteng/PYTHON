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

def process1(figure, t, data):
    FREQS = [(750, 1100)]
    SN = 8000
    fft_data = nf.fft(data) / len(data)

    INDEX = []
    for x in FREQS:
        begin_index = x[0] / ((SN * 1.0) / len(fft_data))
        end_index =   x[1] / ((SN * 1.0) / len(fft_data))
        INDEX.append((begin_index, end_index))
        begin_index_v = len(fft_data) - end_index
        end_index_v   = len(fft_data) - begin_index
        INDEX.append((begin_index_v, end_index_v))

    print(INDEX)

    for x in range(0, len(fft_data)):
        for y in INDEX:
            if x >= y[0] and x <= y[1]:
                fft_data[x] = 0

    data = nf.ifft(fft_data) * len(data)
    wavfile.write('./{}_out.wav'.format(figure), SN, np.int16(data))
    return (t, data)

def show2(figure, t1, data1, t2, data2):
    print('data1: {}\nt1: {}\ndata2: {}\nt2: {}'.format(
        len(data1), len(t1), len(data2), len(t2)))
    plt.figure(figure)
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

def main():
    t1, data1  = read_wav('./bad.wav')
    t2, data2 = process1('remove', t1, data1)
    show2('remove_a', t1, data1, t2, data2)
    plt.show()

if __name__ == '__main__':
    main()
