import cv2

# Загружаем изображение
image = cv2.imread('man1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Находим углы Харриса
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)

# Находим центры масс объектов
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(gray)

# Находим области SIFT
sift = cv2.SIFT_create()
keypoints = sift.detect(gray, None)
sift_image = cv2.drawKeypoints(gray, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Наложение углов Харриса, центров масс и областей SIFT на изображение
image[corners > 0.01 * corners.max()] = [255, 0, 0]  # красный для углов Харриса
for center in centroids[1:]:
    cv2.circle(image, (int(center[0]), int(center[1])), 5, (0, 255, 0), -1)  # Зеленый для центров масс
image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # области SIFT

# Вывод изображения
cv2.imshow('Image with Features', image)
cv2.waitKey(0)
cv2.destroyAllWindows()