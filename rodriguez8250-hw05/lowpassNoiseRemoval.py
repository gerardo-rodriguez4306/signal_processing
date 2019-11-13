# Gerardo Rodriguez - UTA ID: 1001428250

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import soundfile as sf

data, sampling_rate = sf.read('P_9_2.wav')
lpf_cutoff = 7500
filter_length = 101
def init_lpf(w):
     i = 0
     m = len(w) - 1
     while i < len(w):
          if i != (m/2):
               w[i] = np.sin(2*np.pi*(lpf_cutoff/sampling_rate)*(i-(m/2)))/(np.pi*(i-(m/2)))
          else:
               w[i] = 2*(float(lpf_cutoff/sampling_rate))
          i+=1
def init_hamming_window(window):
     i = 0
     m = len(window) - 1
     while i < len(window):
          window[i] = 0.54 - 0.46*np.cos((2*np.pi*i)/m)
          i+=1
def element_wise_product(list_1, list_2, list_result):
     i = 0
     while i < len(list_result):
          list_result[i] = list_1[i] * list_2[i]
          i = i + 1

h_n = np.zeros(filter_length)
init_lpf(h_n)
not_windowed_response = np.convolve(data, h_n)
x, y = freqz(h_n, 1)
plt.plot(x, abs(y), label='original')

w_n = np.zeros(filter_length)
init_hamming_window(w_n)
final_filter = np.zeros(filter_length)
element_wise_product(h_n, w_n, final_filter)
windowed_response = np.convolve(data, final_filter)
x, y = freqz(final_filter, 1)
plt.plot(x, abs(y), label='windowed')
plt.title('Frequency Response')
plt.legend(loc='upper right')
plt.show()

sf.write('cleanMusic.wav', windowed_response, sampling_rate)
