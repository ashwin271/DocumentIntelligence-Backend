import cv2 as cv
import numpy as np


# Preprocessing the image
# image - image to be processed
# NOISE_REMOVE - 1 to remove noise, 0 to keep noise
# x - threshold value (value used to choose which pixels to keep and which to discard)
# y - max value (from my understanding this is brightness control)
def process(file_name, NOISE_REMOVE=0, x=150, y=230):
    file_path = f"./uploaded_documents/{file_name}"
    image = cv.imread(file_path)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.threshold(image, x, y, cv.THRESH_BINARY)[1]

    if NOISE_REMOVE:
        kernel = np.ones((1, 1), np.uint8)
        image = cv.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv.erode(image, kernel, iterations=1)
        image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
        # image = cv.medianBlur(image, 3)

    return image
