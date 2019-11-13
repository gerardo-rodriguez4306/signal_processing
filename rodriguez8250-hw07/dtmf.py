# Gerardo Rodriguez - UTA ID: 1001428250

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
from scipy import signal

def bandpass(bandpass_frequency, filter_length, fs):
     result = np.zeros(filter_length)
     i = 0
     while i < filter_length:
          result[i] = (2.0/L) * np.cos((bandpass_frequency * 2 * np.pi * i)/fs)
          i+=1
     return result
def un_normalize_response(x, fs):
     i = 0
     while i < len(x):
          x[i] = x[i] * fs/(2*np.pi)
          i+=1
     return x
def plot(x,y):
     plt.plot(x,abs(y))
     plt.xlabel('Hertz')
     plt.title('Frequency Responses of Bandpass Filters')
def processTones(name, L, fs, samplesPerTone) :
     frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])

     buttons = [['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['*','0','#']]

     len_freq = len(frequencies)
     filters = np.zeros((7,L))
     file_input = np.loadtxt(open(name), delimiter=",")
     length_input = len(file_input)
     i = 0
     while i < len_freq:
          filters[i] = bandpass(frequencies[i], L, fs)
          i+=1

     output = np.zeros((7, L + length_input - 1))
     i = 0
     while i < len_freq:
          output[i] = np.convolve(filters[i], file_input)
          i+=1
     i = 0
     while i < len_freq:
          x, y = freqz(filters[i], 1)
          x = un_normalize_response(x, fs)
          plot(x,y)
          i+=1
     
     plt.show(block=False)
     plt.pause(1)
     plt.close()
     i = 0
     results = []
     while i < length_input/samplesPerTone:
          means = np.zeros(len_freq)
          j = 0
          while j < len_freq:
               means[j] = np.mean(output[j][i*samplesPerTone:(i+1)*samplesPerTone]**2)
               j+=1
          temp = [None,None]
          temp[0] = np.argmax(means); means[np.argmax(means)] = 0;
          temp[1] = np.argmax(means)
          results.append(temp)
          i+=1
     i = 0
     while i < len(results):
          if (results[i][0] > results[i][1]):
               temp = results[i][0]
               results[i][0] = results[i][1]
               results[i][1] = temp - 4
          if (results[i][1] > 3):
               results[i][1] -= 4
          i+=1
     result = ""
     i = 0
     while i < len(results):
          result+=buttons[results[i][0]][results[i][1]]
          i+=1
     f, t, Sxx = signal.spectrogram(file_input, fs)
     plt.pcolormesh(t,f,Sxx)
     plt.ylabel('Frequency [Hz}')
     plt.xlabel('Time [sec]')
     plt.show(block=False)
     plt.pause(1)
     plt.close()
     return result

#############  main  #############
if __name__ == "__main__":
    filename = "tones.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone,
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)

    print(phoneNumber)
