# Gerardo Rodriguez - Homework #3

import numpy as np

file_input = np.loadtxt(open("data-communications.csv", "rb"), delimiter=",")
pulse0 = np.ones( 10 )
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
pulse1 = pulse1/np.linalg.norm(pulse1)
signal_count = len(file_input)
total_bits = int(signal_count / 10)
bit_array = [0] * total_bits

i = 0
while i < total_bits:
   a = 1 - abs((file_input[(i*10):(i*10)+10]).dot(pulse0)/(np.linalg.norm(file_input[(i*10):(i*10)+10])*np.linalg.norm(pulse0)))
   b = 1 - abs((file_input[(i*10):(i*10)+10]).dot(pulse1)/(np.linalg.norm(file_input[(i*10):(i*10)+10])*np.linalg.norm(pulse1)))
   if a < b:
      c = 0
   else:
      c = 1
   bit_array[i] = c
   i = i + 1

number_of_chars = int(total_bits / 8)
message = np.zeros(number_of_chars)
i = 0
while i < number_of_chars:
   single_byte_array = bit_array[(i*8):((i*8)+8)]
   ascii_character = 0
   msb_to_lsb = 7
   byte_iterator = 0
   while msb_to_lsb > -1:
      ascii_character += (2**msb_to_lsb) * single_byte_array[byte_iterator]
      msb_to_lsb -= 1
      byte_iterator += 1
   ascii_character = chr(int(ascii_character))
   print(ascii_character,end="")
   i += 1
