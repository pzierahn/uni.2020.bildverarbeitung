import math
import skimage.io
import numpy as np


def rgb_zu_cmy(rgb: np.array) -> np.array:
    cmy = 1 - (np.copy(rgb) / 0xff)
    return cmy


def cmy_zu_rgb(cmy: np.array) -> np.array:
    rgb = (1 - np.copy(cmy)) * 0xff
    return rgb.astype(np.uint8)


def rgb_zu_hsi(rgb: np.array) -> np.array:
    hsi = np.zeros(rgb.shape)

    for inx in range(0, rgb.shape[0]):
        for iny in range(0, rgb.shape[1]):

            sum = np.sum(rgb[inx][iny])

            r = int(rgb[inx][iny][0]) / 0xff
            g = int(rgb[inx][iny][1]) / 0xff
            b = int(rgb[inx][iny][2]) / 0xff

            # print(rgb[inx][iny])

            i = sum / 3
            minimum = np.min(rgb[inx][iny]) / 0xff
            s = 1 - (3 / (r + g + b + 0.000001) * minimum)

            print("minimum", minimum)

            # print("r", r)
            # print("g", g)
            # print("b", b)

            hue = (0.5 * ((r - g) + (r - b))) / ((((r - g) ** 2 + ((r - b) * (g - b))) ** 0.5) + 1)
            # hue = 0.5 * ((r - g) + (r - b)) / math.sqrt((r - g) ** 2 + ((r - b) * (g - b)))
            hue = math.cos(hue) ** -1

            if b > g:
                hue = ((360 * math.pi) / 180.0) - hue

            print(rgb[inx][iny])
            print("hue", hue)
            print("s", s)
            print("i", i / 360)

            # top = 0.5 * ((r - g) + (r - b))
            # bottom = ((r - g) ** 2) + (r - b) * (g - b)
            # bottom = bottom ** 0.5
            #
            # theta = math.cos(top / bottom) ** -1
            #
            # h = 360 - theta if b > g else theta

            # hsi[inx][iny] = [hue, s, i]

            exit(0)
    return hsi


def hsi_zu_rgb(hsi: np.array) -> np.array:
    rgb = np.zeros(hsi.shape)

    for inx in range(0, hsi.shape[0]):
        for iny in range(0, hsi.shape[1]):
            i = hsi[inx][iny][2]
            s = hsi[inx][iny][1]
            h = hsi[inx][iny][0]

            b = i * (1 - s)
            r = i * (1 + ((s * math.cos(h)) / (math.cos(60 - h))))
            g = 3 * i - (r + b)

            rgb[inx][iny] = [r, g, b]

    return rgb


rgb = np.array(skimage.io.imread("mandrillFarbe.png"), np.uint8)
# skimage.io.imsave("bv.exercise.05.03.cmy.png", rgb_zu_cmy(rgb))
# skimage.io.imsave("bv.exercise.05.03.rgb.png", cmy_zu_rgb(rgb_zu_cmy(rgb)))

# skimage.io.imsave("bv.exercise.05.03.hsi.png", rgb_zu_hsi(rgb))
skimage.io.imsave("bv.exercise.05.03.rgb.png", hsi_zu_rgb(rgb_zu_hsi(rgb)))
