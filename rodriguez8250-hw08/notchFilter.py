import numpy as np
import matplotlib.pyplot as plt
def plot(x, y, xlim, ylim):
     if xlim != None:
          plt.xlim(xlim)
     if ylim != None:
          plt.ylim(ylim)
     plt.plot(x, y)
     plt.show()
def generate_signal(x, fs, f):
     result = np.cos(2*np.pi*x*(f/fs))
     return result;
def applyNotch(fs, dataFile) :
     f = 17
     input_file = np.loadtxt(open(dataFile), delimiter=",")
     length_input = len(input_file)
     x_axis = np.arange(0, length_input, 1)
     y = np.zeros(length_input + 100)
     i = 0
     w_norm = (2 * np.pi * f) / fs
     while i < length_input + 100:
          if i - 2 >= 0:
               y[i] = y[i] + (-1 * 0.8783 * y[i - 2])
               if i - 2 < length_input:
                    y[i] = y[i] + (1 * input_file[i - 2])
          if i - 1 >= 0:
               y[i] = y[i] + (1.8744 * np.cos(w_norm) * y[i - 1] )
               if i - 1 < length_input:
                    y[i] = y[i] + (-2 * np.cos(w_norm) * input_file[i - 1])
          if i < length_input:
               y[i] = y[i] + (input_file[i])
          i+=1
     x_lim = [-25, 625]
     y_lim = [-2.25, 2.25]
     plot(x_axis, input_file, x_lim, None)
     x_axis = np.arange(0,len(y), 1)
     plot(x_axis, y, None, y_lim)
     x_axis = np.arange(0, length_input, 1)
     ten_hertz = generate_signal(x_axis,fs, 10)
     thirty_three_hertz = generate_signal(x_axis,fs, 33)
     mixed_signal = ten_hertz + thirty_three_hertz
     plot(x_axis, mixed_signal, x_lim, None)
############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
