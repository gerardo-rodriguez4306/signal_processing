# Description of the Problem
Standard analog phones generate dual-tone multifrequency signals when a specific key is pressed. For this example, we were given a comma-separated-value file that contained samples of a generated tone. To determine which key was pressed, we generated a filter bank with defined frequencies to filter out. 

## Runtime Behavior

![script.gif](script.gif)

Above, you'll find the runtime behavior of *script.sh* that tests the `csv` files and prints the specified keys within the `csv` file.

## Libraries Used

- `numpy` is used for its `ndarray` objects, its `loadtxt` method, its `argmax` method to determine which frequency passed through the bandpass filters, and its `convolve` method.

- `matplotlib.pyplot` is used for plotting.

- `scipy` is used for its `freqz` function and its `spectrogram` function.
