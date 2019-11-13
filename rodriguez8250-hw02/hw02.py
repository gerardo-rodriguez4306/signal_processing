# Gerardo Rodriguez - Homework 2

# Library importations
import soundfile as sf
import numpy as np

# constant declarations and initializations

x = np.arange(0,12, 1.0/8000) # creating 96,000 sample points
iterator = list(range(4000, 100000, 4000)) # iterates through the frequency array during waveform creation
C = 52; D = 54; E = 56; F = 57; G = 59; A = 61 # notes with their associated key value
notes = [C, C, G, G, A, A, G, G, F, F, E, E, D, D, E, C, G, G, F, F, E, E, D, D]
number_of_notes = len(notes)
frequency_array = [None]*number_of_notes
i = 0
while (i < number_of_notes):
     frequency_array[i] = 440 * 2**((notes[i] - 49)/12)
     i = i + 1

# waveform creation
y = [None]*len(x)
i = 0; j = 0;
while (j < 96000):
     y[j] = np.cos(2*np.pi*frequency_array[i] * x[j]) # cos( w_0 * discrete_time_point)
     j = j + 1
     if (j in iterator): # if our iterated value is a multiple of 4000 (96,000 / 4000 == 24 ---> # of notes in sequence)
          i = i + 1
          y[j-3] = y[j-2] = y[j-1] = 0 # added pauses between notes because sheet music is non legato

sf.write('twinkle.wav', y, 8000)
