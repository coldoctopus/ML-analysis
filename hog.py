import pandas as pd
from skimage.feature import hog
import cv2
import os
from os import listdir

def preprocessing(filePath):
    data = []
    label = []

    csv_path = filePath + "\labels.csv"
    imgList = pd.read_csv(csv_path, index_col=0)

    # ['surprise' 'anger' 'disgust' 'fear' 'sad' 'contempt' 'neutral' 'happy']

    for index, row in imgList.iterrows():
        directory = filePath + "/" + str(row['pth'])

        #resize and config the image
        image = cv2.imread(directory)
        image = cv2.resize(image , (200, 200))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Compute HOG features
        hog_features = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)

        data.append(hog_features)
        label.append(row['label'])

    return data , label





