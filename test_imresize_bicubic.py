import time

import cv2
import numpy as np
import torch

from bicubic_pytorch import imresize as imresize_bic
from matlab_functions import imresize

# read images
img = cv2.imread('imresize_bicubic/baboon.png') / 255.
test_times = 1

# test using our imresize
print('test using our imresize...')
for mode in ['down', 'up']:
    for scale in [2, 3, 4]:
        if mode == 'down':
            resize_scale = 1 / scale
        else:
            resize_scale = scale
        start_time = time.time()
        for i in range(test_times):
            img_resize = imresize(img, resize_scale, antialiasing=True)
        avg_time = (time.time() - start_time) / test_times
        img_resize = np.clip((img_resize * 255).round(), 0, 255)
        img_resize_matlab = cv2.imread(
            f'imresize_bicubic/baboon_{mode}_x{scale}_matlab.png')
        diff = img_resize - img_resize_matlab
        diff_abssum = np.sum(np.abs(diff))
        h, w, _ = img_resize_matlab.shape
        diff_ratio = diff_abssum / (h * w) * 100
        print(f'Mode {mode} X {scale}. Diff: {int(diff_abssum):d},'
              f' {diff_ratio:.2f}%. Time: {avg_time}.')


def imresize_np(img, resize_scale, antialiasing):
    if type(img).__module__ == np.__name__:  # numpy type
        numpy_type = True
        img = torch.from_numpy(img.transpose(2, 0, 1)).float()
    out = imresize_bic(img, resize_scale, antialiasing=True)
    if numpy_type:
        out = out.numpy().transpose(1, 2, 0)
    return out


# test using bicubic_pytorch
print('test using bicubic_pytorch...')
for mode in ['down', 'up']:
    for scale in [2, 3, 4]:
        if mode == 'down':
            resize_scale = 1 / scale
        else:
            resize_scale = scale
        start_time = time.time()
        for i in range(test_times):
            img_resize = imresize_np(img, resize_scale, antialiasing=True)
        avg_time = (time.time() - start_time) / test_times
        img_resize = np.clip((img_resize * 255).round(), 0, 255)
        img_resize_matlab = cv2.imread(
            f'imresize_bicubic/baboon_{mode}_x{scale}_matlab.png')
        diff = img_resize - img_resize_matlab
        diff_abssum = np.sum(np.abs(diff))
        h, w, _ = img_resize_matlab.shape
        diff_ratio = diff_abssum / (h * w) * 100
        print(f'Mode {mode} X {scale}. Diff: {int(diff_abssum):d},'
              f' {diff_ratio:.2f}%. Time: {avg_time}.')
