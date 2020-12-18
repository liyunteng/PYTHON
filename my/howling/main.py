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
    # data = data / 32768.0
    # data = np.reshape(data, [nframes, nchannels])
    print('framerate: {}\nnchannels: {}\nnframes: {}\n'.format(
        framerate, nchannels, nframes))
    t = np.arange(0, nframes) * (1.0 / framerate)
    print('time({}s): {}'.format(1.0 / 8000 * len(t), t))
    print('data: {}\n'.format(data))
    return(t, data)

def process1(figure, t, data):
    N = 160
    FS = 8000
    THRESHOLD = 0.1
    COUNTER = 100
    NQ = 30

    counter = 0
    begin = 0
    end = N
    pre = [ 0 ] * N
    C = [ 0 ] * N
    S = [ 0 ] * N
    out = []
    A = [ 0 ] * N
    V = []


    data = data / 32768.0
    while begin < len(data):
        print('{} -- {}'.format(begin, end))
        fft_data = nf.fft(data[begin:end]) / (end - begin)
        v = [ 0 ] * len(fft_data)
        for x in range(0, len(fft_data)):
            v[x] = fft_data[x] - pre[x]
            pre[x] = fft_data[x]
        V.append(v)
        if len(V) > NQ:
            del V[0]

        for x in range(0, len(fft_data)):
            fa = []
            for v in V:
                fa.append(v[x])

            std = np.std(fa)
            S[x] = std
            if std > THRESHOLD:
                C[x] += 1
                fft_data[x] = 0
                # print('sec: {} std: {} c: {} counter:{} freq: {}'.format(
                #     counter * 0.02, std, C[x], counter,
                #     x * (1.0 * 8000)/len(fft_data)))
            else:
                C[x] -= 1
                # fft_data[x] = 0
                # print('sec: {} std: {} c: {} counter: {} freq: {}'.format(
                #     counter * 0.02, std, C[x], counter,
                #     x * (1.0 * 8000) / len(fft_data)
                # ))
            if C[x] == NQ:
                pass
                # fft_data[x] = 0
                # C[x] -= 1
                # print('sec: {} std: {} c: {} counter: {} freq: {}'.format(
                #     counter * 0.02, std, C[x], counter,
                #     x * (1.0 * 8000) / len(fft_data)
                # ))

        freqs = np.abs(nf.fftfreq(end-begin, 1.0 / 8000))
        samples = np.arange(0, end-begin)
        if counter % 50 == 0:
            plt.figure(figure)

            plt.subplot(321)
            plt.xlabel('Sample')
            plt.ylabel('Signal')
            plt.grid(linestyle=':')
            plt.plot(samples, data[begin:end])

            plt.subplot(322)
            plt.xlabel('Freq')
            plt.ylabel('Power')
            plt.grid(linestyle=':')
            plt.plot(freqs, fft_data)

            plt.subplot(323)
            plt.xlabel('Sample')
            plt.ylabel('V(f)')
            plt.grid(linestyle=':')
            plt.plot(samples, v)

            plt.subplot(324)
            plt.xlabel('Freq')
            plt.ylabel('V(f)')
            plt.grid(linestyle=':')
            plt.plot(freqs, v)
            # print(np.array(V))

            plt.subplot(325)
            plt.xlabel('Sample')
            plt.ylabel('STD(f)')
            plt.grid(linestyle=':')
            plt.plot(samples, S)

            plt.subplot(326)
            plt.xlabel('Freq')
            plt.ylabel('STD(f)')
            plt.grid(linestyle=':')
            plt.plot(freqs, S)

            # plt.subplot(616)
            # plt.xlabel('Freq')
            # plt.ylabel('counter')
            # plt.grid(linestyle=':')
            # plt.bar(freqs, C)

        out += (nf.ifft(fft_data).real * (end -begin) * 32768.0).tolist()

        begin = end
        if end + N > len(data):
            end = len(data)
        else:
            end += N
        counter += 1

    print('counter: {}\n'.format(counter))
    wavfile.write('./{}_out.wav'.format(figure), 8000, np.int16(out))
    return (t, out)

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
    t2, data2 = process1('bad', t1, data1)
    show2('bad_a', t1, data1, t2, data2)

    t1, data1  = read_wav('./good.wav')
    t2, data2 = process1('good', t1, data1)
    show2('good_a', t1, data1, t2, data2)
    plt.show()

if __name__ == '__main__':
    main()
