from PIL import Image, ImageDraw, ImageFilter,ImageChops
# Открываем изображение
im = Image.open('man1.jpg')

# Размытие исходного изображения
#blurred = im.filter(ImageFilter.BLUR)
blurred = im.filter(ImageFilter.GaussianBlur(radius=1.2))

# Вычисляем разницу между исходным и размытым изображениями
sharp = ImageChops.difference(im, blurred)
sharp = ImageChops.add(im, sharp)

# Сохраняем результат
sharp.save('sharp_color_man.jpg')

# Создаем новое изображение для отображения всех трех: оригинал, маска нерезкости, улучшенное по резкости
result_im = Image.new('RGB', (im.width * 3, im.height))
result_im.paste(im, (0, 0))
result_im.paste(blurred, (im.width, 0))
result_im.paste(sharp, (im.width * 2, 0))


# Отображаем результат
result_im.show()



#### Повторим то же самое для полутонового изображения
# Открываем изображения


# Открываем изображение
im_ovcharka = Image.open('ovcharka.jpg').convert('L')

# Размытие исходного изображения
#blurred_voron = im_voron.filter(ImageFilter.BLUR)
blurred_ovcharka = im_ovcharka.filter(ImageFilter.GaussianBlur(radius=1.8))

# Вычисляем разницу между исходным и размытым изображениями
sharp_ovcharka = ImageChops.difference(im_ovcharka, blurred_ovcharka)
sharp_ovcharka = ImageChops.add(im_ovcharka, sharp_ovcharka)

# Сохраняем результат
sharp_ovcharka.save('sharp_bw_ovcharka.jpg')

# Создаем новое изображение для отображения всех трех: оригинал, маска нерезкости, улучшенное по резкости
result_im_ovcharka = Image.new('RGB', (im_ovcharka.width * 3, im_ovcharka.height))
result_im_ovcharka.paste(im_ovcharka, (0, 0))
result_im_ovcharka.paste(blurred_ovcharka, (im_ovcharka.width, 0))
result_im_ovcharka.paste(sharp_ovcharka, (im_ovcharka.width * 2, 0))


# Отображаем результат
result_im_ovcharka.show()
result_im_ovcharka.save('2result.jpg')