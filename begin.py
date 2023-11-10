import pandas as pd
from skimage.feature import hog
import cv2

def hog_feat(directory):
    image = cv2.imread(directory)
    image = cv2.resize(image , (200, 200))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hog_features, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(10, 10), visualize=True)
    return hog_features


