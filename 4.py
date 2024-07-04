from PIL import Image
import numpy as np
import cv2

# Открываем изображение
im = Image.open('harris.jpg')

# Преобразуем изображение в оттенки серого
gray = im.convert('L')

# Преобразуем изображение в массив numpy
img = np.array(gray)

# Вычисляем производные в каждом пикселе с использованием гауссова сглаживания
img_smooth = cv2.GaussianBlur(img, (5, 5), 0)

# Вычисляем градиенты по оси x и y
Ix = cv2.Sobel(img_smooth, cv2.CV_64F, 1, 0, ksize=3)
Iy = cv2.Sobel(img_smooth, cv2.CV_64F, 0, 1, ksize=3)

# Вычисляем матрицы вторых моментов M
Ix2 = Ix**2
Iy2 = Iy**2
Ixy = Ix * Iy

# Сглаживаем матрицы вторых моментов M по окну 3x3
kernel = np.ones((3, 3), np.float32) / 9
Sxx = cv2.filter2D(Ix2, -1, kernel)
Syy = cv2.filter2D(Iy2, -1, kernel)
Sxy = cv2.filter2D(Ixy, -1, kernel)

# Вычисляем отклик угла R
k = 0.04
R = Sxx * Syy - Sxy**2 - k * (Sxx + Syy)**2

# Отрезаем по порогу R
threshold = 0.1 * np.max(R)
corners = np.argwhere(R > threshold)

# Объединяем близкие точки в одну, если расстояние между ними меньше определенного значения
min_distance = 3.61
grouped_corners = []
for corner in corners:
    new_corner = True
    for grouped_corner in grouped_corners:
        if np.linalg.norm(corner - grouped_corner) < min_distance:
            grouped_corner += corner
            grouped_corner //= 2
            new_corner = False
            break
    if new_corner:
        grouped_corners.append(corner)

# Выводим углы на исходном изображении
color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for corner in grouped_corners:
    cv2.circle(color_img, tuple(corner[::-1]), 5, (255, 0, 255), -1)


print(f"Количество обнаруженных углов: {len(grouped_corners)}")
# Изменяем размер изображения на 600x600
resized_img = cv2.resize(color_img, (600, 600))

# Отображаем измененное изображение с подсвеченными углами
cv2.imshow('Corners Detected (Resized)', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()