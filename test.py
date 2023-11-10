import pandas as pd
from skimage.feature import hog
import cv2


data = []
label = []
directory = "D:/dataset/anger/image0000356.jpg"

filePath = "D:/dataset"
csv_path = filePath + "\labels.csv"
imgList = pd.read_csv(csv_path, index_col=0)

#resize and config the image
image = cv2.imread(directory)
image = cv2.resize(image , (200, 200))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute HOG features
hog_features, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(10, 10), visualize=True)

data.append(hog_features)


print(data)

print(imgList.iloc[0:30])