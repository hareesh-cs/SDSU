import numpy as np
import cv2

image = cv2.imread('red_rose.jpg')  # reading image using opencv library
grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # converting the color image to grayscaled image
grayscaled = cv2.merge([grayscaled, grayscaled, grayscaled])  # combining all single channel images to make a multi-channel image
cv2.imshow('grayscaled',grayscaled)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # converting the color image to hsv image

# setting limits to select the color
lower_limit = np.array([90, 70, 40])
upper_limit = np.array([255, 255, 255])
limits = cv2.inRange(hsv_image, lower_limit, upper_limit)

colored_image = cv2.bitwise_and(image, image, mask=limits) # selecting the image in between limits of color image
gray_image = cv2.bitwise_and(grayscaled, grayscaled, mask=255-limits)
singleColorHighlighted = colored_image+gray_image

cv2.imshow('colored_output', colored_image)
cv2.imwrite('colored_output_red.jpg', colored_image)
cv2.imshow('gray_output', gray_image)
cv2.imwrite('gray_output_red.jpg', gray_image)
cv2.imshow('singleColorHighlighted', singleColorHighlighted)
cv2.imwrite('singleColorHighlighted_red.jpg', singleColorHighlighted)
cv2.waitKey()