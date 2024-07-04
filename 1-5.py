from PIL import Image, ImageDraw, ImageEnhance, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


# Открываем изображение
image_path = "example.jpg"  # Укажите путь к вашему изображению
image = Image.open(image_path)

# Номер 1. Выводим информацию об изображении
print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Режим изображения:", image.mode)

# 2. Создаем цветную миниатюру (произвольный размер)
thumbnail_color = image.copy()
thumbnail_color.thumbnail((555, 370))  # Укажите размер миниатюры
thumbnail_color.save("thumbnail_color.jpg")  # Сохраняем миниатюру

thumbnail_bw = image.convert("L")  # Преобразуем в чёрно-белое изображение
thumbnail_bw.thumbnail((555, 370))  # Укажите размер миниатюры
thumbnail_bw.save("thumbnail_bw.jpg")  # Сохраняем миниатюру

# 3.
x = 250
y = 150
size = 150
def rotate_square_region(image, x, y, size, angle):
    x = 250
    y = 150
    size = 150
    region = image.crop((x, y, x + size, y + size))
    rotated_region_90 = region.rotate(90)
    rotated_region_125 = region.rotate(-125)

    image.paste(rotated_region_90, (x, y))
    image.paste(rotated_region_125, (x, y))

    draw = ImageDraw.Draw(image)
    draw.rectangle([x, y, x + size, y + size], outline="red")
    draw.rectangle([x, y, x + size, y + size], outline="blue")

    return image


# 4. Загрузка полутонового изображения
image = Image.open("example.jpg").convert("L")
image_array = np.array(image)

inverted_image_array = 255 - image_array
inverted_image = Image.fromarray(inverted_image_array)

plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.title('Histogram - Original Image')

plt.subplot(2, 2, 3)
plt.imshow(inverted_image, cmap='gray')
plt.title('Inverted Image')

plt.subplot(2, 2, 4)
plt.hist(inverted_image_array.flatten(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.title('Histogram - Inverted Image')

plt.tight_layout()
plt.savefig('histograms.png')
plt.show()


# 5. Отображение по оси Y и изменение яркости
pil_image = Image.open('example.jpg')
reflected_image = pil_image.transpose(Image.FLIP_LEFT_RIGHT).convert('L')

# Преобразование в массивы NumPy
image_array = np.array(reflected_image)
reflected_array = np.array(reflected_image)

# Увеличение яркости отраженного изображения
brightened_reflected_array = np.clip(reflected_array + 135, 0, 255).astype(np.uint8)
brightened_reflected_image = Image.fromarray(brightened_reflected_array)

# Построение гистограмм
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(reflected_array.flatten(), bins=256, range=(0, 255), density=True, color='gray', alpha=0.75)
plt.xlabel('Яркость пикселей')
plt.ylabel('Частота')
plt.title('Гистограмма отраженного изображения')

plt.subplot(1, 2, 2)
plt.hist(brightened_reflected_array.flatten(), bins=256, range=(0, 255), density=True, color='gray', alpha=0.75)
plt.xlabel('Яркость пикселей')
plt.ylabel('Частота')
plt.title('Гистограмма отраженного высветленного изображения')

plt.tight_layout()

# Отображение изображений
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(reflected_array, cmap='gray')
plt.axis('off')
plt.title('Отраженное изображение')

plt.subplot(1, 2, 2)
plt.imshow(brightened_reflected_array, cmap='gray')
plt.axis('off')
plt.title('Отраженное высветленное изображение')

plt.tight_layout()
reflected_image.save("reflected_image.jpg")
brightened_reflected_image.save("brightened_reflected_image.jpg")
plt.show()




# Загрузка исходного изображения
input_image = Image.open("example.jpg")

# Изменение квадратной области и добавление цветных границ
output_image = rotate_square_region(input_image, 100, 100, 200, 45)

# Сохранение результата
output_image.save("output_image.jpg")

