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

            #
            # Transformationsfunktion
            #
            # histogram[0] -> Wahrscheinlichkeitswerte
            # sum(histogram[0]) = 1
            #
            index = bild[inx][iny]
            equalize_bild[inx][iny] = round(0xff * np.sum(histogram[0][:index]))

    return equalize_bild


bild1 = np.array(skimage.io.imread("bildverbesserung/bild1.png"), np.uint8)
equal = equalize_hist(bild1)
skimage.io.imsave("bv.exercise.06.04.bild1.equal.png", equal)

bild2 = np.array(skimage.io.imread("bildverbesserung/bild2.png"), np.uint8)
equal = equalize_hist(bild2)
skimage.io.imsave("bv.exercise.06.04.bild2.equal.png", equal)
