import math
import skimage.io
import skimage.exposure
import numpy as np
import matplotlib.pyplot as plt


def equalize_hist(bild: np.array) -> np.array:
    histogram = np.histogram(bild, bins=255, range=(0, 256), density=True)

    equalize_bild = np.zeros(bild.shape, np.uint8)

    for inx in range(bild.shape[0]):
        for iny in range(bild.shape[1]):

            index = bild[inx][iny]
            equalize_bild[inx][iny] = round(0xff * np.sum(histogram[0][:index]))

    return equalize_bild


bild1 = np.array(skimage.io.imread("bildverbesserung/bild1.png"), np.uint8)
bild2 = np.array(skimage.io.imread("bildverbesserung/bild2.png"), np.uint8)

equal = equalize_hist(bild1)
skimage.io.imsave("bv.exercise.06.04.bild1.equal.png", equal)

# histogram1 = np.histogram(bild1, bins=255, range=(0, 256), density=True)
# print("histogram1", histogram1)
#
# plt.figure(0)
# plt.hist(bild1.flatten(), bins=255, range=(0, 256), density=True)
# plt.savefig("bv.exercise.06.04.bild1.png")



# soll_bild1 = skimage.exposure.equalize_hist(bild1)
# skimage.io.imsave("bv.exercise.06.04.bild1.soll.png", soll_bild1)
#
# soll_bild2 = skimage.exposure.equalize_hist(bild2)
# skimage.io.imsave("bv.exercise.06.04.bild2.soll.png", soll_bild2)
