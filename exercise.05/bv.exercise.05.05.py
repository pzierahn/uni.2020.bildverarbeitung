import math
import skimage.io
import numpy as np
import matplotlib.pyplot as plt

# 1. Ladet das Bild mandrillFarbe.png aus dem Moodle und zeigt es an.
img = np.array(skimage.io.imread("mandrillFarbe.png"), np.uint8)
skimage.io.imsave("bv.exercise.05.05.01.png", img)

# 2. Invertiert das Bild, indem ihr jeden Farbwert einzeln im RGB-Modell invertiert.
# Welche Farben des Ursprungsbildes werden dabei auf welche Farben im neuen Bild abgebildet?

maske = np.ones(img.shape) * 0xff
invertiert = maske - img
skimage.io.imsave("bv.exercise.05.05.02.png", invertiert)

# 3. Zerlegt das Bild in seine einzelnen Farbkanäle als Graustufenbilder
# und zeigt diese an. Was sagen euch die Helligkeitswerte in den drei Einzelbildern?

skimage.io.imsave("bv.exercise.05.05.03.red.png", img[:, :, 0])
skimage.io.imsave("bv.exercise.05.05.03.green.png", img[:, :, 1])
skimage.io.imsave("bv.exercise.05.05.03.blue.png", img[:, :, 2])

# 4. Setzt nun die drei Farbkanäle wieder zusammen zu einem RGB-Bild.
# Tauscht dabei aber die Kanäle Rot und Blau.
# Wie verändert sich das Bild und warum ist das so?

red = np.copy(img[:, :, 0])
# green = np.copy(img[:, :, 1])
blue = np.copy(img[:, :, 2])

switchImg = np.copy(img)
switchImg[:, :, 0] = blue
switchImg[:, :, 2] = red

skimage.io.imsave("bv.exercise.05.05.04.png", switchImg)
