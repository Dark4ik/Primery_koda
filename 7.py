import cv2
import matplotlib.pyplot as plt
import numpy as np

# Загрузка изображения
img = cv2.imread('man1.jpg')

# Преобразование изображения в RGB формат
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Применение сдвига по x и y
M_shift = np.float32([[1, 0, 50], [0, 1, 30]])
img_shifted = cv2.warpAffine(img, M_shift, (img.shape[1], img.shape[0]), borderMode=cv2.BORDER_REPLICATE)

# Применение поворота на 45 градусов
M_rotate = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 45, 1)
img_rotated = cv2.warpAffine(img, M_rotate, (img.shape[1], img.shape[0]), borderMode=cv2.BORDER_REPLICATE)

# Применение масштабирования в 2.5 раза
M_scale = np.float32([[2.5, 0, 0], [0, 2.5, 0]])
img_scaled = cv2.warpAffine(img, M_scale, (int(img.shape[1]*1.5), int(img.shape[0]*1.5)), borderMode=cv2.BORDER_REPLICATE)

# Отображение изображений
plt.figure(figsize=(12, 12))
plt.subplot(221)
plt.imshow(img_shifted)
plt.title('Сдвиг по x и y')

plt.subplot(222)
plt.imshow(img_rotated)
plt.title('Поворот на 45 градусов')

plt.subplot(223)
plt.imshow(img_scaled)
plt.title('Масштабирование в 2.5 раза')

plt.show()