# Gerardo Rodriguez - UTA ID: 1001428250

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import soundfile as sf
def processFile(fn, offset) :
     data, sampling_rate = sf.read(filename)
     data_fft = np.fft.fft(data)
     midpoint = len(data_fft)/2
     i = int(midpoint - offset)
     x_values = np.arange(0,len(data), 1)
     plt.subplot(1,2,1)
     plt.title('Original Signal')
     plt.xlabel('Frequency [Hz]')
     plt.ylabel('Amplitude')
     plt.plot(x_values, abs(data_fft))
     plt.subplot(1,2,2)
     while (i < midpoint + offset):
          data_fft[i] = 0
          i+=1
     clean_data = np.fft.ifft(data_fft)
     clean_fft = np.fft.fft(clean_data)
     plt.title('Clean Signal')
     plt.plot(x_values, abs(clean_fft))
     plt.xlabel('Frequency [Hz]')
     plt.ylabel('Amplitude')
     plt.tight_layout()
     plt.show()
     sf.write('cleanMusic.wav', np.real(clean_data), sampling_rate)
##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 9500

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
