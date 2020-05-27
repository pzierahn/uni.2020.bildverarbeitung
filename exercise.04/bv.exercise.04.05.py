import math
import skimage.io
import numpy as np


def get_nearest_neighbor_interpolation(img: np.array, x_point: float, y_point: float) -> np.array:
    x_min = max(0, math.floor(x_point))
    x_max = min(img.shape[0] - 1, math.floor(x_point + 1))

    y_min = max(0, math.floor(y_point))
    y_max = min(img.shape[1] - 1, math.floor(y_point + 1))

    x_min_color_avg = (img[x_min][y_min] / 2) + (img[x_min][y_max] / 2)
    x_max_color_avg = (img[x_max][y_min] / 2) + (img[x_max][y_max] / 2)

    y_min_color_avg = (img[x_min][y_min] / 2) + (img[x_max][y_min] / 2)
    y_max_color_avg = (img[x_min][y_max] / 2) + (img[x_max][y_max] / 2)

    x_min_distance = x_point - math.floor(x_point)
    y_min_distance = y_point - math.floor(y_point)

    x_weighted_color = (x_min_color_avg * x_min_distance) + (x_max_color_avg * (1 - x_min_distance))
    y_weighted_color = (y_min_color_avg * y_min_distance) + (y_max_color_avg * (1 - y_min_distance))

    return (x_weighted_color + y_weighted_color) / 2


def scale_img(img: np.array, scale: float) -> np.array:
    print("img.shape", img.shape)
    print("img.shape", np.array(img.shape) * scale)

    newShape = (int(img.shape[0] * scale), int(img.shape[1] * scale))
    newImg = np.empty(newShape)
    print("newImg.shape", newImg.shape)

    x_scale = img.shape[0] / newShape[0]
    y_scale = img.shape[1] / newShape[1]

    for inx in range(newShape[0]):
        for iny in range(newShape[1]):
            x_point = inx * x_scale
            y_point = iny * y_scale

            newImg[inx][iny] = get_nearest_neighbor_interpolation(img, x_point, y_point)

    return newImg


img = np.array(skimage.io.imread("tv.png"), np.uint8)
newImg = scale_img(img, 2.7)
skimage.io.imsave("tv.new.png", newImg)
