# Gerardo Rodriguez - UTA ID: 1001428250

from PIL import Image
import numpy as np
from scipy import ndimage

filtered_photo = Image.open('darinGrayNoise.jpg')
filtered_photo.show(title="With Salt and Pepper")
filtered_array = np.array(filtered_photo)
unfiltered_array = ndimage.median_filter(filtered_array, 5)
unfiltered_photo = Image.fromarray(unfiltered_array)
unfiltered_photo.show(title="Without Salt and Pepper")
