import skimage.io
import skimage.color
import numpy as np

bild1 = np.array(skimage.io.imread("blumen/image_02881.jpg"), np.uint8)
bild1_maske = np.array(skimage.io.imread("blumen/image_02881_maske.png"), np.uint8)

bild1_hsi = skimage.color.rgb2hsv(bild1)

bild2 = np.array(skimage.io.imread("blumen/image_02890.jpg"), np.uint8)
bild2_maske = np.array(skimage.io.imread("blumen/image_02890_maske.png"), np.uint8)

bild3 = np.array(skimage.io.imread("blumen/image_04650.jpg"), np.uint8)
bild3_maske = np.array(skimage.io.imread("blumen/image_04650_maske.png"), np.uint8)

bild4 = np.array(skimage.io.imread("blumen/image_04666.jpg"), np.uint8)
bild4_maske = np.array(skimage.io.imread("blumen/image_04666_maske.png"), np.uint8)


#
# 1.
#

def img_grey_mean_mask(img: np.array, maske: np.array) -> int:
    grey = skimage.color.rgb2gray(img)
    maskedImg = np.ma.array(grey, mask=1 - maske)

    return np.ma.mean(maskedImg)


print("Mittleren Grauwert Bild 1 =", img_grey_mean_mask(bild1, bild1_maske))
print("Mittleren Grauwert Bild 2 =", img_grey_mean_mask(bild2, bild2_maske))
print("Mittleren Grauwert Bild 3 =", img_grey_mean_mask(bild3, bild3_maske))
print("Mittleren Grauwert Bild 4 =", img_grey_mean_mask(bild4, bild4_maske))


#
# 2.
#

def img_hsi_mean_mask(img: np.array, maske: np.array) -> []:
    hsv = skimage.color.rgb2hsv(img)
    masked_h = np.ma.array(hsv[:, :, 0], mask=1 - maske)
    masked_s = np.ma.array(hsv[:, :, 1], mask=1 - maske)
    masked_i = np.ma.array(hsv[:, :, 2], mask=1 - maske)

    return [
        np.ma.mean(masked_h),
        np.ma.mean(masked_s),
        np.ma.mean(masked_i),
    ]


print("Mittleren Farbton Bild 1 =", img_hsi_mean_mask(bild1, bild1_maske))
print("Mittleren Farbton Bild 2 =", img_hsi_mean_mask(bild2, bild2_maske))
print("Mittleren Farbton Bild 3 =", img_hsi_mean_mask(bild3, bild3_maske))
print("Mittleren Farbton Bild 4 =", img_hsi_mean_mask(bild4, bild4_maske))

