import albumentations as A
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

image = Image.open('image.jpg')
# print(f'PIL before convert', image.size)
image = image.convert('RGB')  # needed for normalzie. W/o it there are w*h*4
# print(f'PIL after convert', image.size)

image = np.array(image)

transform = A.Compose([
    # A.RandomResizedCrop(256, 256),
    A.LongestMaxSize(256),
    # A.SmallestMaxSize(256),
    # A.Normalize(),
    # A.RandomCrop(256, 256),
    # A.CLAHE(),  # sharpness
    # A.CoarseDropout(), # rectangular
    # A.ColorJitter(),  # color aug
    # A.Cutout(),  # square
    # A.Equalize(), # color aug
    # A.HorizontalFlip(),
    # A.HueSaturationValue(10, 10, 10, p=1)  # color aug
    # Pad side of the image/max if side is less than desired number
    A.PadIfNeeded(256, 256, border_mode=cv2.BORDER_CONSTANT),
    # A.RandomBrightness(),
    # A.RandomContrast(),
    # A.RandomBrightnessContrast(),
    # A.RandomGridShuffle(),  # Random shuffle grid's cells on image.
    # A.RGBShift(),
    # A.Sharpen(), # removed?
    # A.ToGray(),
    # A.Transpose() # same as flip horizontally
    # A.VerticalFlip(),
    # A.CenterCrop(256, 256),
])

augmentations = transform(image=image)
image = augmentations['image']

print(f'dims after augs', image.shape)

plt.imshow(image)
plt.show()
