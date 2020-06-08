import math
import skimage.io
import skimage.color
import numpy as np
import matplotlib.pyplot as plt

# 1. Ladet das Bild mandrillFarbe.png aus dem Moodle und zeigt es an.
img = np.array(skimage.io.imread("mandrillFarbe.png"), np.uint8)
skimage.io.imsave("bv.exercise.05.04.01.png", img)

# 2. Invertiert das Bild, indem ihr jeden Farbwert einzeln im RGB-Modell invertiert.
# Welche Farben des Ursprungsbildes werden dabei auf welche Farben im neuen Bild abgebildet?

maske = np.ones(img.shape) * 0xff
invertiert = maske - img
skimage.io.imsave("bv.exercise.05.04.02.png", invertiert)

# 3. Zerlegt das Bild in seine einzelnen Farbkanäle als Graustufenbilder
# und zeigt diese an. Was sagen euch die Helligkeitswerte in den drei Einzelbildern?

skimage.io.imsave("bv.exercise.05.04.03.red.png", img[:, :, 0])
skimage.io.imsave("bv.exercise.05.04.03.green.png", img[:, :, 1])
skimage.io.imsave("bv.exercise.05.04.03.blue.png", img[:, :, 2])

# 4. Setzt nun die drei Farbkanäle wieder zusammen zu einem RGB-Bild.
# Tauscht dabei aber die Kanäle Rot und Blau.
# Wie verändert sich das Bild und warum ist das so?

red = np.copy(img[:, :, 0])
# green = np.copy(img[:, :, 1])
blue = np.copy(img[:, :, 2])

switchImg = np.copy(img)
switchImg[:, :, 0] = blue
switchImg[:, :, 2] = red

skimage.io.imsave("bv.exercise.05.04.04.png", switchImg)

# 5. Wandelt das RGB-Bild in ein Grauwertbilder um. Nehmt dabei an, dass sich der Grauwert je
# Pixel als Mittelwert der drei Farbwerte an dieser Position berechnet.

grau = np.zeros((img.shape[0], img.shape[1]))

for inx in range(0, img.shape[0]):
    for iny in range(0, img.shape[1]):
        grau[inx][iny] = np.mean(img[inx][iny])

skimage.io.imsave("bv.exercise.05.04.05.png", grau)

# 6. Wie verändert sich das Bild, wenn ihr die Sättigung des Bildes voll aufdreht (1) oder komplett
# herunterdreht (0)? Probiert es aus und erklärt die Veränderungen.

saettigung = np.copy(img)
saettigung = skimage.color.rgb2hsv(saettigung)

for inx in range(0, saettigung.shape[0]):
    for iny in range(0, saettigung.shape[1]):
        saettigung[inx][iny][2] = 0

saettigung = skimage.color.hsv2rgb(saettigung)
skimage.io.imsave("bv.exercise.05.04.06.0.png", saettigung)

# 7. Verändert die Farbtöne (hue) des Bildes indem ihr alle Farbtöne im Bild um jeweils ...

# farbton = np.copy(img)
# farbton = skimage.color.rgb2hsv(farbton)
#
# saettigung = np.copy(img)
# saettigung = skimage.color.rgb2hsv(saettigung)
#
# for inx in range(0, saettigung.shape[0]):
#     for iny in range(0, saettigung.shape[1]):
#
#         print("rgb", img[inx][iny])
#         print("hsv", saettigung[inx][iny])
#         print("hsv", 360 * 0.14157706)
#
#         saettigung[inx][iny][0] = ((60 / 360) + saettigung[inx][iny][0]) % 1
#         exit(0)
#
# saettigung = skimage.color.hsv2rgb(saettigung)
# skimage.io.imsave("bv.exercise.05.04.06.png", saettigung)
#

