import math

import numpy as np
import cv2

original_img = cv2.imread('img.jpg')
print("Shape of the original image is", original_img.shape)
h, w, p = original_img.shape
k = int(input("please enter value of k > 1:"))
resampled_img = np.zeros((k * h, k * w, p), np.uint8)
for i in range(k * h):
    for j in range(k * w):
        x = i / k if k > 1 else 1
        y = j / k if k > 1 else 1

        x_f = math.floor(x)
        x_c = min(h - 1, math.ceil(x))
        y_f = math.floor(y)
        y_c = min(w - 1, math.ceil(y))

        if (x_c == x_f) and (y_c == y_f):
            q = original_img[int(x), int(y), :]
        elif x_c == x_f:
            q1 = original_img[int(x), int(y_f), :]
            q2 = original_img[int(x), int(y_c), :]
            q = q1 * (y_c - y) + q2 * (y - y_f)
        elif y_c == y_f:
            q1 = original_img[int(x_f), int(y), :]
            q2 = original_img[int(x_c), int(y), :]
            q = (q1 * (x_c - x)) + (q2 * (x - x_f))
        else:
            v1 = original_img[x_f, y_f, :]
            v2 = original_img[x_c, y_f, :]
            v3 = original_img[x_f, y_c, :]
            v4 = original_img[x_c, y_c, :]

            q1 = v1 * (x_c - x) + v2 * (x - x_f)
            q2 = v3 * (x_c - x) + v4 * (x - x_f)
            q = q1 * (y_c - y) + q2 * (y - y_f)

        resampled_img[i, j, :] = q
cv2.imshow('original image', original_img)
cv2.imshow("resampled_img", resampled_img.astype(np.uint8))
print("Shape of resampled image is: ", resampled_img.shape)
cv2.imwrite('resampled_img1.jpg', resampled_img)
cv2.waitKey()