import cv2
import numpy as np
from scipy.ndimage import label
import numpy as np
import imageio.v2 as imageio
from scipy import ndimage
import matplotlib.pyplot as plt

im = np.array(cv2.imread('man1.jpg', 0))
labeled_im, num_features = label(im)

print('Количество объектов:', num_features)

# открываем изображение в полутонах
image = imageio.imread('utki.jpg', mode='L')
# пороговое значение 180 для бинаризации изображения
threshold_value = 180
#пиксели, значения которых меньше порогового значения, устанавливаются в 1, а остальные - в 0.
binary_image = np.where(image < threshold_value, 1, 0)
# операция бинарного открытия
opened_image = ndimage.binary_opening(binary_image)
# метка объектов для пометки связанных пикселей на открытом изображении
objects, num_objects = ndimage.label(opened_image)
print('Количество объектов:', num_objects)
f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
plt.title('Оригинальное изображение')
plt.axis("off")
f.add_subplot(1, 2, 2)
plt.imshow(opened_image)
plt.title("Измененное изображение")
plt.axis("off")
plt.show(block=True)
