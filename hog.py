import numpy as np
import cv2, os
from PIL import Image
from skimage import color, feature, io

'''
def preprocessing(filePath):
    data = []
    label = []
    face = ['anger'] #, 'happy', 'neutral', 'sad', 'suprise'
    for expression in face:
        directory = os.path.join(filePath, expression) #directory to each folder consisting of different expressions
        data_listing = os.listdir(directory)    #a list of path to each image
        for file in data_listing:
            #open image in the main dataset folder + subfolder, then config them
            image = Image.open(os.path.join(directory, file))
            image = color.rgb2gray(np.array(image))
            image = cv2.resize(image, (200, 200))

            #build hog feat.
            hog_features = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False, multichannel=False)

            #add them to lists
            data.append(hog_features)
            label.append(expression)

    return data, label
'''



def preprocessing(filePath):
    data = []
    label = []
    face = ['anger', 'happy', 'neutral', 'sad', 'suprise']  #
    for expression in face:
        directory = os.path.join(filePath, expression)  # use os.path.join for joining paths
        data_listing = os.listdir(directory)  # a list of path to each image
        for file in data_listing:
            # open image in the main dataset folder + subfolder, then config them
            image = io.imread(os.path.join(directory, file))
            if len(image.shape) > 2 and image.shape[2] == 3:
                image = color.rgb2gray(image)
            image = cv2.resize(image, (200, 200))

            # build hog feat.
            hog_features = feature.hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False)

            # add them to lists
            data.append(hog_features)
            label.append(expression)

    return data, label

'''
path = "D:\Bao\Document\_VGU\Intro to CS\dataset"
data, label = preprocessing(path)
print(len(data))'''