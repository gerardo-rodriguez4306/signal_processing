# Gerardo Rodriguez - UTA ID: 1001428250

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.feature import match_template

def rgb_to_gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def show(image):
    gray_image = rgb_to_gray(image)
    show_img = Image.fromarray(gray_image)
    show_img.show()
    return gray_image
  
def findImage(mainImage, template):
     original = Image.open(mainImage)
     original_array = np.array(original)
     template = Image.open(template)
     template_array = np.array(template)
    
     gray_original = show(original_array)
     gray_template = show(template_array)
    
     result = match_template(gray_original, gray_template)
     row = np.argmax(np.max(result, axis=0))
     column = np.argmax(np.max(result, axis=1))
     gray_original[column : column + len(gray_template), row : row + len(gray_template)] = 0
     show_img = Image.fromarray(gray_original)
     show_img.show()
     return row, column;
  
#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))


