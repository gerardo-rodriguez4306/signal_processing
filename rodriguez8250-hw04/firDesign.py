# Gerardo Rodriguez - UTA ID: 1001428250

import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 2000
lpf_cutoff = 50
hpf_cutoff = 280
filter_length = 21

def init_lpf(w):
     i = 0
     m = len(w) - 1
     while i < m + 1: # len(w) = m + 1
          if i != (m/2):
               w[i] = np.sin(2*np.pi*(lpf_cutoff/sampling_rate)*(i-(m/2))/(np.pi*(i-(m/2))))
          else:
               w[i] = 2*lpf_cutoff/sampling_rate
          i+=1

def init_hpf(w):
     i = 0
     m = len(w) - 1
     while i < len(w):
          if i != (m/2):
               w[i] = - np.sin(2*np.pi*(hpf_cutoff/sampling_rate)*(i - (m/2)))/(np.pi*(i-(m/2)))
          else:
               w[i] = 1 - 2*(hpf_cutoff/sampling_rate)
          i+=1

file_input = np.loadtxt(open("data-filtering.csv", "rb"), delimiter=",")
x = np.arange(0, sampling_rate, 1)
four_hertz_signal = np.cos(2*np.pi*x*(4/sampling_rate))
three_hundred_hertz_signal = np.cos(2*np.pi*x*(300/sampling_rate))
w = np.zeros(filter_length)

# lpf
init_lpf(w)
lpf_signal = np.convolve(w, file_input)
twenty_points = np.arange(2000, 2020, 1)
x_2 = np.append(x, twenty_points)
plt.subplot(3,1,1)
plt.title("original signal")
plt.plot(x, file_input)
plt.subplot(3,1,2)
plt.title("4 Hz signal")
plt.plot(x, four_hertz_signal)
plt.subplot(3,1,3)
plt.title("application of lowpass filter")
plt.tight_layout()
plt.plot(x_2,lpf_signal)
plt.show()

# lpf
init_hpf(w)
hpf_signal = np.convolve(w, file_input)
plt.subplot(3,1,1)
plt.title("original signal")
plt.plot(x, file_input)
plt.xlim(0,100)
plt.subplot(3,1,2)
plt.title("330 Hz signal")
plt.plot(x, three_hundred_hertz_signal)
plt.xlim(0,100)
plt.subplot(3,1,3)
plt.title("application of highpass filter")
plt.tight_layout()
plt.plot(x_2,hpf_signal)
plt.xlim(0,100)
plt.show()
