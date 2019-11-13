# Gerardo Rodriguez - UTA ID: 1001428250
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob

def element_wise_subtraction(v_1, v_2):
     length_v1 = len(v_1)
     result = np.zeros(length_v1)
     i = 0
     while i < length_v1:
          result[i] = v_1[i] - v_2[i]
          i+=1
     return result

def one_norm(vector):
     length = len(vector)
     result = 0
     i = 0
     while i < length:
          result += abs(vector[i])
          i+=1
     return result

def classifyMusic() :
     input_data, fs = sf.read('testSong.wav')
     file_names = glob.glob("song-*")
     database_size = len(file_names)
     f, t, Sxx_input = spectrogram(input_data, fs=fs, nperseg=fs//2)
     i = 0
     time_segments = len(t)
     input_signature = []

     while i < time_segments:
          input_signature.append( np.argmax(Sxx_input[:, i]) * 2.0)
          i+=1
     input_signature = np.array(input_signature)
     comparison_signatures = np.zeros((database_size, time_segments))

     i = 0
     while i < database_size:
          temp_result = []
          j = 0
          current_song, fs_comparison = sf.read(file_names[i])
          f_comparison, t_comparison, Sxx_comparison = spectrogram(current_song, fs=fs_comparison, nperseg=fs_comparison//2)
          while j < time_segments:
               temp_result.append( np.argmax(Sxx_comparison[:,j]) * 2)
               j+=1
          comparison_signatures[i] = np.array(temp_result)
          i+=1
     list_of_norms = np.zeros(database_size)

     i = 0
     while i < database_size:
          list_of_norms[i] = one_norm( element_wise_subtraction( comparison_signatures[i], input_signature )  )
          i+=1
     
     i = 0
     min_array = [None] * 5
     while i < len(min_array):
          min_array[i] = np.argmin(list_of_norms)
          print("%d  %s" %(list_of_norms[min_array[i]], file_names[min_array[i]]))
          list_of_norms[min_array[i]] = list_of_norms[np.argmax(list_of_norms)]
          i+=1
     i = 0
     plt.figure("testSong.wav")
     plt.specgram(input_data, Fs=fs)
     plt.show(block=False)
     plt.pause(1)
     plt.close()
     while i < 2:
          current_song, fs_comparison = sf.read(file_names[min_array[i]])
          plt.figure(file_names[min_array[i]])
          plt.specgram(current_song, Fs=fs_comparison)
          plt.show(block=False)
          plt.pause(1)
          plt.close()
          i+=1
          
###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
