import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
# 7
image = Image.open('example.jpg').convert('L')
image.save("7_example.jpg")
image_array = np.array(image)

noise = np.random.normal(loc=0, scale=30, size=image_array.shape).astype(np.uint8)#Генерирует случайный шум с нормальным распределением (среднее 0, стандартное отклонение 30)
noisy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)
# Создает зашумленное изображение путем добавления шума к исходному изображению.
# Ограничивает значения пикселей в диапазоне от 0 до 255, чтобы избежать переполнения.
# Преобразует значения пикселей в беззнаковые целые числа (uint8).

noisy_image = Image.fromarray(noisy_image_array)

hist, bins = np.histogram(image_array.flatten(), bins=256, range=(0, 256))
hist_noisy, _ = np.histogram(noisy_image_array.flatten(), bins=256, range=(0, 256)) #Вычисляет гистограмму зашумленного изображения с таким же количеством бинов и диапазоном

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.plot(hist, color='blue')
plt.title('Гистограмма оригинального изображения')
plt.xlabel('Яркость пикселя')
plt.ylabel('Частота')

plt.subplot(1, 2, 2)
plt.plot(hist_noisy, color='red')
plt.title('Гистограмма изображения с шумом')
plt.xlabel('Яркость пикселя')
plt.ylabel('Частота')

plt.tight_layout()
noisy_image.save('noisy_image.png')
plt.show()

# 8
sigma_values = [1, 5, 9] # значения сигм для фильтра Гаусса
blurred_images = [gaussian_filter(image_array, sigma=sigma) for sigma in sigma_values]

plt.figure(figsize=(15, 5))
for i, blurred_image in enumerate(blurred_images):
    plt.subplot(1, len(sigma_values), i+1)
    plt.imshow(blurred_image, cmap='gray')
    plt.contour(blurred_image, colors='black', linewidths=1) #Добавляет контур к изображению blurred_image с черным цветом и шириной линии 1.
    plt.title(f'Сигма = {sigma_values[i]}')
    plt.axis('off')

plt.tight_layout()
plt.show()
