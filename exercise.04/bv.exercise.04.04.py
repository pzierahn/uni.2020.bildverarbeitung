import math
import skimage.io
import numpy as np

scale = 2.3

img = np.array(skimage.io.imread("tv.png"), np.uint8)
print("img.shape", img.shape)
print("img.shape", np.array(img.shape) * scale)

newShape = (int(img.shape[0] * scale), int(img.shape[1] * scale))
newImg = np.empty(newShape)
print("newImg.shape", newImg.shape)

x_scale = img.shape[0] / newShape[0]
y_scale = img.shape[1] / newShape[1]


def get_nearest_neighbor(inx: int, iny: int) -> (int, int):
    x_point = inx * x_scale
    y_point = iny * y_scale

    x_min = max(0, math.floor(x_point))
    x_max = min(img.shape[0], math.floor(x_point + 1))

    y_min = max(0, math.floor(y_point))
    y_max = min(img.shape[1], math.floor(y_point + 1))

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


for inx in range(newShape[0]):
    for iny in range(newShape[1]):
        newImg[inx][iny] = img[get_nearest_neighbor(inx, iny)]

skimage.io.imsave("tv.new.png", newImg)
