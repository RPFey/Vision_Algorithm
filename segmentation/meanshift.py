from sklearn.cluster import MeanShift
import numpy as np
import random

class MeanShift_Segmentation(MeanShift):
    """
        MeanShift Segmentation Using sklearn meanshift class
    
    """
    def __init__(self, **args):
        super().__init__(**args)

    def segment_image(self, image:np.ndarray):
        """
        Segment a given image

        image (np.ndarray):
            input image
        
        """
        # get the shape of the image
        height = image.shape[0]
        width = image.shape[1]
        # Construct Mesh grid 
        x = np.arange(width)
        y = np.arange(height)
        X, Y = np.meshgrid(x, y)
        X = X.reshape(-1, 1)
        Y = Y.reshape(-1, 1)
        # concatenate features -- (R, G, B, X, Y)
        image_feature = image.reshape((-1, 4))
        features = np.concatenate([image_feature, X, Y], axis = 1)
        # fit model
        self.fit(features)

        # obtain each segment
        uniq_label = np.unique(self.labels_)
        label_image = np.array((height * width, 3), np.uint8)
        # assign a unique color
        for item in uniq_label:
            value = np.random.randint(0, 255, size=(3, ), dtype=np.uint8)
            loc = np.where(self.labels_ == item)
            label_image[loc] = value

        label_image = label_image.reshape((height, width, 3))
        return label_image