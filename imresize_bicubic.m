% read the test image
img = imread('imresize_bicubic/baboon.png');
img = im2double(img);
test_times = 1;
elapsed_time = zeros(test_times,1);

% downsample x2
for i = 1:test_times
    t = tic;
    img_down_x2 = imresize(img, 1/2, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_down_x2, 'imresize_bicubic/baboon_down_x2_matlab.png');

% downsample x3
for i = 1:test_times
    t = tic;
    img_down_x3 = imresize(img, 1/3, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_down_x3, 'imresize_bicubic/baboon_down_x3_matlab.png');

% downsample x4
for i = 1:test_times
    t = tic;
    img_down_x4 = imresize(img, 1/4, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_down_x4, 'imresize_bicubic/baboon_down_x4_matlab.png');

% upsample x2
for i = 1:test_times
    t = tic;
    img_up_x2 = imresize(img, 2, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_up_x2, 'imresize_bicubic/baboon_up_x2_matlab.png');

% upsample x3
for i = 1:test_times
    t = tic;
    img_up_x3 = imresize(img, 3, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_up_x3, 'imresize_bicubic/baboon_up_x3_matlab.png');

% upsample x4
for i = 1:test_times
    t = tic;
    img_up_x4 = imresize(img, 4, 'bicubic');
    t = toc(t);
    elapsed_time(i) = t;
end
time_avg = mean(elapsed_time)
imwrite(img_up_x4, 'imresize_bicubic/baboon_up_x4_matlab.png');

