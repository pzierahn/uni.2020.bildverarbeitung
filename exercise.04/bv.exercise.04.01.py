import math
import skimage.io
import numpy as np
import matplotlib.pyplot as plt

img1 = np.array(skimage.io.imread("bild1.png"), np.uint8)
img2 = np.array(skimage.io.imread("bild2.png"), np.uint8)
img3 = np.array(skimage.io.imread("bild3.png"), np.uint8)

# plt.imshow(img1, cmap='gray', vmin=0, vmax=255)

newImg = np.log(np.ones(img1.shape) + img1)

plt.imshow(newImg, cmap='gray', vmin=0, vmax=255)
