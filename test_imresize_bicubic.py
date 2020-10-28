import cv2
import numpy as np

from matlab_functions import imresize

# read images
img = cv2.imread('imresize_bicubic/baboon.png') / 255.

# downsample x2
img_down_x2 = imresize(img, 1 / 2, antialiasing=True)
img_down_x2 = (img_down_x2 * 255).round()
img_down_x2_matlab = cv2.imread('imresize_bicubic/baboon_down_x2_matlab.png')
diff = img_down_x2 - img_down_x2_matlab
diff_abssum = np.sum(np.abs(diff))
h, w, _ = img_down_x2_matlab.shape
diff_ratio = diff_abssum / (h * w) * 100
print(diff_abssum, diff_ratio)

# downsample x3
img_down_x3 = imresize(img, 1 / 3, antialiasing=True)
img_down_x3 = (img_down_x3 * 255).round()
img_down_x3_matlab = cv2.imread('imresize_bicubic/baboon_down_x3_matlab.png')
diff = img_down_x3 - img_down_x3_matlab
diff_abssum = np.sum(np.abs(diff))
h, w, _ = img_down_x3_matlab.shape
diff_ratio = diff_abssum / (h * w) * 100
print(diff_abssum, diff_ratio)

# downsample x4
img_down_x4 = imresize(img, 1 / 3, antialiasing=True)
img_down_x4 = (img_down_x4 * 255).round()
img_down_x4_matlab = cv2.imread('imresize_bicubic/baboon_down_x4_matlab.png')
diff = img_down_x4 - img_down_x4_matlab
diff_abssum = np.sum(np.abs(diff))
h, w, _ = img_down_x4_matlab.shape
diff_ratio = diff_abssum / (h * w) * 100
print(diff_abssum, diff_ratio)
