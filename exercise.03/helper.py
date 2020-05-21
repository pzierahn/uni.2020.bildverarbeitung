import math
import skimage.io
import matplotlib.pyplot as plt
import numpy as np


def c(img):
    result = np.zeros_like(img)
    result[:, :] = np.max(img)
    return result


def e(img):
    return img[:, 1:] - img[:, :-1]


img = skimage.io.imread("../exercise.02/mandrill.png")
print(img)
print(c(img))
plt.imshow(c(img))

skimage.io.imsave("mandrill-e.png", e(img))
skimage.io.imsave("mandrill-e-1.png", img[:, 1:])
skimage.io.imsave("mandrill-e--1.png", img[:, :-1])
