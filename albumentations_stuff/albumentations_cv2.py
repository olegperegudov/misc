# albumentations runs on cv2

import albumentations as A
import cv2

# Declare an augmentation pipeline
transform = A.Compose([
    # A.RandomResizedCrop(256, 256),
    # A.LongestMaxSize(256),
    A.SmallestMaxSize(256),
    A.RandomCrop(256, 256),
    # A.CLAHE(),
    # A.CoarseDropout(), # rectangular
    # A.ColorJitter(),
    # A.Cutout(), # square
    # A.Equalize(),
    # A.HorizontalFlip(),
    # A.HueSaturationValue(10, 10, 10)
    # A.PadIfNeeded(256, 256), # Pad side of the image / max if side is less than desired number.
    # A.RandomBrightness(),
    # A.RandomBrightnessContrast(),
    # A.RandomContrast(),
    # A.RandomGridShuffle(),  # Random shuffle grid's cells on image.
    # A.RGBShift(),
    # A.Sharpen(), # removed?
    # A.ToGray(),
    # A.Transpose() # same as flip horizontally
    # A.VerticalFlip(),
    # A.CenterCrop(256, 256),
])

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]
print(image.shape)

cv2.imshow('image', transformed_image)
cv2.waitKey(0)
