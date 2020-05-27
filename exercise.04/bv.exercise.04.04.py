import math
import skimage.io
import numpy as np

def get_nearest_neighbor(shape: tuple, x_point: float, y_point: float) -> (int, int):

    x_min = max(0, math.floor(x_point))
    x_max = min(shape[0], math.floor(x_point + 1))

    y_min = max(0, math.floor(y_point))
    y_max = min(shape[1], math.floor(y_point + 1))

    dist = float("inf")
    pixel = (0, 0)

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            xxx = np.linalg.norm(np.array([x_point, y_point])
                                 - np.array([x, y]))

            if xxx < dist:
                pixel = (x, y)
                dist = xxx

    return pixel


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

            newImg[inx][iny] = img[get_nearest_neighbor(img.shape, x_point, y_point)]

    return newImg


img = np.array(skimage.io.imread("tv.png"), np.uint8)
newImg = scale_img(img, 0.5)
newImg2 = scale_img(newImg, 2)
skimage.io.imsave("tv.new.png", newImg2)
