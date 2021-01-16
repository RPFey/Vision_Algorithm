from segmentation import MeanShift_Segmentation
import skimage.io
import matplotlib.pyplot as plt

model = MeanShift_Segmentation(bandwidth = 1, n_jobs = 4)
image = skimage.io.imread("./test/data/mountain.png")

mask = model.segment_image(image)
plt.figure()
plt.imshow(mask)
plt.show()

