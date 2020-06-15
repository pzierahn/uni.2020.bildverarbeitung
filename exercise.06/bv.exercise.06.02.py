import numpy
import skimage.io


def formel_1(bild: numpy.array):
    cols = bild.shape[0]
    rows = bild.shape[1]

    mean = 0

    for inx in range(cols):
        for iny in range(rows):
            mean += bild[inx][iny]

    mean /= cols * rows

    standard_deviation = 0

    for inx in range(cols):
        for iny in range(rows):
            standard_deviation += (bild[inx][iny] - mean) ** 2

    standard_deviation /= cols * rows

    print("Formel 1")
    print("mean", mean)
    print("standard_deviation", standard_deviation)


def formel_2(bild: numpy.array):
    cols = bild.shape[0]
    rows = bild.shape[1]

    mean = 0
    standard_deviation = 0

    for inx in range(cols):
        for iny in range(rows):
            mean += bild[inx][iny]
            standard_deviation += bild[inx][iny] ** 2

    mean /= cols * rows
    standard_deviation = (standard_deviation / (cols * rows)) - (mean ** 2)

    print("Formel 2")
    print("mean", mean)
    print("standard_deviation", standard_deviation)


bild = skimage.io.imread("mandrill.png")
formel_1(bild)
formel_2(bild)

# print("bild", bild)
# print("bild", type(bild))
