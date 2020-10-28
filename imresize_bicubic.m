% read the test image
img = imread('imresize_bicubic/baboon.png');
img = im2double(img);

% downsample x2
img_down_x2 = imresize(img, 1/2, 'bicubic');
imwrite(img_down_x2, 'imresize_bicubic/baboon_down_x2_matlab.png');

% downsample x3
img_down_x3 = imresize(img, 1/3, 'bicubic');
imwrite(img_down_x3, 'imresize_bicubic/baboon_down_x3_matlab.png');

% downsample x4
img_down_x4 = imresize(img, 1/4, 'bicubic');
imwrite(img_down_x4, 'imresize_bicubic/baboon_down_x4_matlab.png');

% upsample x2
img_up_x2 = imresize(img, 2, 'bicubic');
imwrite(img_up_x2, 'imresize_bicubic/baboon_up_x2_matlab.png');

% upsample x3
img_up_x3 = imresize(img, 3, 'bicubic');
imwrite(img_up_x3, 'imresize_bicubic/baboon_up_x3_matlab.png');

% upsample x4
img_up_x4 = imresize(img, 4, 'bicubic');
imwrite(img_up_x4, 'imresize_bicubic/baboon_up_x4_matlab.png');

