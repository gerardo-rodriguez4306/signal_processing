# Description of the Problem
Music identification has been addressed by the application Shazam. This program, a bare-bones version of Shazam, identifies music by applying the one-norm to the element-wise array difference of a song to the sample taken.
## Runtime Behavior
![script gif](script.gif)

Above, you'll find the runtime behavior of *script.sh* that tests test files and compares them against the 64-song database.

## Libraries Used

- Numpy is used primarily for its `ndarray` objects but its `argmin` and `argmax` methods are also used to determine which one-norms are smallest and which frequencies are most prominent, respectively.

- `matplotlib.pyplot` is used for plotting.

- `numpy.linalg` is included for its `norm` function but I wrote my own one-norm function.

- `soundfile` is used to process the `.wav` files.

- `scipy.signal` is used to produce spectrograms for frequency analysis.

- `glob` is used to analyze the current working directory for files of interest.
