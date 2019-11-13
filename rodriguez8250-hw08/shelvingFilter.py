import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def applyShelvingFilter(inName, outName, g, fc) :
     data, sampling_rate = sf.read(inName)
     normalized_cutoff = (2 * np.pi * fc) / sampling_rate
     mu = 10**(g/20)
     gamma = (1-(4/(1+mu))*np.tan(normalized_cutoff/2))/(1+(4/(1+mu))*np.tan(normalized_cutoff/2))
     alpha = (1-gamma)/2.0
     length_data = len(data)
     y = np.zeros(length_data)
     u = np.zeros(length_data)
     i = 0
     u[i] = alpha * (data[i])
     i +=1
     while i < length_data:
          u[i] = alpha * (data[i] +data[i-1]) + gamma * (u[i-1])
          i+=1
     i = 0
     while i < length_data:
          y[i] = data[i] + (mu - 1)*u[i]
          i+=1
     fft_data = np.fft.fft(data)
     fft_filtered = np.fft.fft(y)
     max_val = np.amax(abs(fft_data))
     x = np.arange(0, len(fft_data), 1)
     plt.subplot(1,2,1)
     plt.title('original signal')
     plt.xlabel('Hz')
     plt.plot(x, abs(fft_data))
     plt.xlim([0,len(fft_data)/4])
     plt.ylim([0, abs(max_val) + 100])
     plt.subplot(1,2,2)
     plt.title('filtered signal')
     plt.xlabel('Hz')
     plt.plot(x, abs(fft_filtered))
     plt.xlim([0, len(fft_filtered)/4])
     plt.ylim([0, abs(max_val) + 100])
     plt.show()
     sf.write(outName, y, sampling_rate)

##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
