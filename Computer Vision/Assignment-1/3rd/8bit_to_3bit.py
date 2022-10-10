import cv2
import numpy as np

image_8bit = cv2.imread('8bit_cherry.jpg')  # reading image
image_8bit = np.uint8(image_8bit)
print("Max Value: {}, Image Size: {}, Shape: {}".format(image_8bit.max(), image_8bit.size, image_8bit.shape))
image_3bit = (image_8bit/2**8)*2**3 # dividing each pixel value
image_3bit = np.uint8(image_3bit)  # typecasting to nd array
print("Max Value: {}, Image Size: {}, Shape: {}".format(image_3bit.max(), image_3bit.size, image_3bit.shape))
upscale = image_3bit * 2**5  # as the 3 bit image is not visible, upscaleing the image by multiplying whole array.
cv2.imshow('3bit_cherry.jpg', image_3bit)
cv2.imshow('3bit_cherry_upscaled.jpg',upscale )
cv2.imwrite('3bit_cherry.jpg', image_3bit)
cv2.imwrite('3bit_cherry_upscaled.jpg',upscale)
cv2.waitKey()