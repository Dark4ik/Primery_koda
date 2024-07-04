
from PIL import Image, ImageDraw

# Открываем изображения
im1 = Image.open('gazon.jpg')
im2 = Image.open('korgi.jpg')


# Создаем новое изображение для наложения
result = Image.new('RGB', im1.size)
result.paste(im1, (0, 0))  # Наложение фона

# Координаты для наложения в произвольной области
x_offset = 300
y_offset = 220
result.paste(im2, (x_offset, y_offset))  # Наложение в произвольной области

# Сохраняем результаты наложения в отдельные файлы
result.save('background_with_image.jpg')  # Сохранение с фоном


# Создаем новое изображение для наложения
result = Image.new('RGB', im1.size)

# Рассчитываем координаты для наложения в центре
x_offset = (im1.width - im2.width) // 2
y_offset = (im1.height - im2.height) // 2

# Наложение изображения в центре
result.paste(im1, (0, 0))  # Наложение фона
result.paste(im2, (x_offset, y_offset))  # Наложение в центре

# Сохраняем результат наложения в отдельный файл
result.save('centered_image.jpg')  # Сохранение с центрированным наложением






im1 = Image.open('mountain.jpg')
im2 = Image.open('ovcharka.jpg')

# Создаем маску из изображения im2

# Наложение маски на произвольное изображение
mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
# задаем форму наложенной картинки
draw.rectangle((100, 20, 500, 380), fill = 1000)
# вставка изображения с маской в фоновое
im1.paste(im2, (0, 0), mask_im)
im1.save('fon_pillow_paste_mask_circle.jpg', quality=95)
