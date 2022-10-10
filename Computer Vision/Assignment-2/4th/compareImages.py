import cv2

imageA = cv2.imread('A.jpg')
grayscaled_A = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
histogram_A = cv2.calcHist([grayscaled_A], [0], None, [256], [0, 256])

imageB = cv2.imread('B.jpg')
grayscaled_B = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
histogram_B = cv2.calcHist([grayscaled_B], [0], None, [256], [0, 256])

imageC = cv2.imread('C.jpg')
grayscaled_C = cv2.cvtColor(imageC, cv2.COLOR_BGR2GRAY)
histogram_C = cv2.calcHist([grayscaled_C], [0], None, [256], [0, 256])

imageD = cv2.imread('D.jpg')
grayscaled_D = cv2.cvtColor(imageD, cv2.COLOR_BGR2GRAY)
histogram_D = cv2.calcHist([grayscaled_D], [0], None, [256], [0, 256])

distance = [0, 0, 0]

# comparing imageA with imageB
i = 0
while i < len(histogram_A) and i < len(histogram_B):
    distance[0] += (histogram_A[i] - histogram_B[i]) ** 2
    i += 1
distance[0] = 100 - (distance[0] ** (1 / 2) / 100)

# comparing imageA with imageC
i = 0
while i < len(histogram_A) and i < len(histogram_C):
    distance[1] += (histogram_A[i] - histogram_C[i]) ** 2
    i += 1
distance[1] = 100 - (distance[1] ** (1 / 2) / 100)

# comparing imageA with imageD
i = 0
while i < len(histogram_A) and i < len(histogram_D):
    distance[2] += (histogram_A[i] - histogram_D[i]) ** 2
    i += 1
distance[2] = 100 - (distance[2] ** (1 / 2) / 100)

closest_image = distance.index(max(distance))

if closest_image == 0:
    print("image B is the most similar image to A with a similarity value of ", distance[0])
elif closest_image == 1:
    print("image C is the most similar image to A with a similarity value of ", distance[1])
else:
    print(" image D is the most similar image to A with a similarity value of ", distance[2])
