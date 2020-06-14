import math
import skimage.io
import skimage.exposure
import numpy as np
import matplotlib.pyplot as plt


def equalize_hist(bild: np.array) -> (np.array, np.array, np.array):
    histogram = np.histogram(bild, bins=256, range=(0, 256), density=True)
    equalize_bild = np.zeros(bild.shape, np.uint8)

    histogram_kumuliert = []

    for inx in range(256):
        histogram_kumuliert += [histogram[0][inx]]

        if inx > 0:
            histogram_kumuliert[inx] += histogram_kumuliert[inx - 1]

    for inx in range(bild.shape[0]):
        for iny in range(bild.shape[1]):
            #
            # Transformationsfunktion
            #
            index = bild[inx][iny]
            equalize_bild[inx][iny] = round(0xff * histogram_kumuliert[index])

    return (equalize_bild, histogram_kumuliert, histogram[0])


bild1 = np.array(skimage.io.imread("bildverbesserung/bild1.png"), np.uint8)
equal, trans1, histo1 = equalize_hist(bild1)
skimage.io.imsave("bv.exercise.06.04.bild1.equal.png", equal)

bild2 = np.array(skimage.io.imread("bildverbesserung/bild2.png"), np.uint8)
equal, trans2, histo2 = equalize_hist(bild2)
skimage.io.imsave("bv.exercise.06.04.bild2.equal.png", equal)

plt.figure(1)
plt.plot(range(len(trans1)), trans1)
# plt.bar(range(len(histo1)), histo1)
plt.legend(["bild1"])
# plt.show()
plt.savefig("bv.exercise.06.04.bild1.transformationsfunk.png", dpi=600)

plt.figure(2)
plt.plot(range(len(trans2)), trans2)
# plt.bar(range(len(histo2)), histo2)
plt.legend(["bild2"])
# plt.show()
plt.savefig("bv.exercise.06.04.bild2.transformationsfunk.png", dpi=600)
