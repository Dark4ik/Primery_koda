import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('example.jpg')

# Применение размытия Гаусса с разными значениями
blurred_image1 = cv2.GaussianBlur(image, (5, 5), 0)
blurred_image2 = cv2.GaussianBlur(image, (9, 9), 0)
blurred_image3 = cv2.GaussianBlur(image, (13, 13), 0)

# Рисование изолиний для разных значений
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image 1', blurred_image1)
cv2.imshow('Blurred Image 2', blurred_image2)
cv2.imshow('Blurred Image 3', blurred_image3)

cv2.waitKey(0)
cv2.destroyAllWindows()