import cv2, os
from skimage import color, feature, io

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
