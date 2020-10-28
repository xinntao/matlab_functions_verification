import cv2
import numpy as np
import torch

from imresize import imresize


def imresize_np(img):
    if type(img).__module__ == np.__name__:  # numpy type
        numpy_type = True
        img = torch.from_numpy(img.transpose(2, 0, 1)).float()
    out = imresize(img)
    if numpy_type:
        out = out.numpy().transpose(1, 2, 0)
    return out


# read images
img = cv2.imread('imresize_bicubic/baboon.png') / 255.

# test
for mode in ['down', 'up']:
    for scale in [2, 3, 4]:
        if mode == 'down':
            resize_scale = 1 / scale
        img_resize = imresize_np(img, resize_scale, antialiasing=True)
        img_resize = (img_resize * 255).round()
        img_resize_matlab = cv2.imread(
            f'imresize_bicubic/baboon_{mode}_x{scale}_matlab.png')
        diff = img_resize - img_resize_matlab
        diff_abssum = np.sum(np.abs(diff))
        h, w, _ = img_resize_matlab.shape
        diff_ratio = diff_abssum / (h * w) * 100
        print(f'Mode {mode} X {scale}. Diff: {int(diff_abssum):d},'
              f' {diff_ratio:.2f}%.')
