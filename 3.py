from PIL import Image, ImageFilter, ImageChops
import numpy as np
import matplotlib.pyplot as plt

# Открываем изображение
im = Image.open('man1.jpg')

# Применяем оператор Собеля
im_sobel = im.filter(ImageFilter.FIND_EDGES)

# Применяем оператор Гаусса
im_gaussian = im.filter(ImageFilter.GaussianBlur)

# Выводим результаты работы операторов
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(im)
plt.title('Исходное изображение')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(im_sobel)
plt.title('Оператор Собеля')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(im_gaussian)
plt.title('Оператор Гаусса')
plt.axis('off')

# Получаем данные для гистограммы
im_array = np.array(im)
im_sobel_array = np.array(im_sobel)
im_gaussian_array = np.array(im_gaussian)

# Строим гистограммы
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(im_array.ravel(), bins=256, color='r', alpha=0.5)
plt.title('Гистограмма исходного изображения')

plt.subplot(1, 3, 2)
plt.hist(im_sobel_array.ravel(), bins=256, color='g', alpha=0.5)
plt.title('Гистограмма оператора Собеля')

plt.subplot(1, 3, 3)
plt.hist(im_gaussian_array.ravel(), bins=256, color='b', alpha=0.5)
plt.title('Гистограмма оператора Гаусса')

plt.show()