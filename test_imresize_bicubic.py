import cv2
import numpy as np

from matlab_functions import imresize

# read images
img = cv2.imread('imresize_bicubic/baboon.png') / 255.

# upsample
for mode in ['down', 'up']:
    for scale in [2, 3, 4]:
        img_resize = imresize(img, 2, antialiasing=True)
        img_resize = (img_resize * 255).round()
        img_resize_matlab = cv2.imread(
            f'imresize_bicubic/baboon_{mode}_x{scale}_matlab.png')
        diff = img_resize - img_resize_matlab
        diff_abssum = np.sum(np.abs(diff))
        h, w, _ = img_resize_matlab.shape
        diff_ratio = diff_abssum / (h * w) * 100
        print(
            f'Mode {mode} X {scale}. Diff: {diff_abssum:d}, {diff_ratio:.2f}%.'
        )
