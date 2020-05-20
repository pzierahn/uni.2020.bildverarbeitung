import math
import skimage.io
import matplotlib.pyplot as plt
import numpy as np

imgF = skimage.io.imread("./findetDieFehler/mitFehler.png")
imgO = skimage.io.imread("./findetDieFehler/ohneFehler.png")

arr1 = np.array(imgF)
arr2 = np.array(imgO)

# 1. Ermittelt zunächst ein Bild, das die Veränderungen
# zwischen den beiden Bildern zeigt als Verküpfung
# der Bilder mit einem sinnvollen arithmetischen Operator.
diff = np.bitwise_xor(arr1, arr2)

# 2. Wandelt das Ergebnis anschließend in ein Binärbild um,
# das veränderte Pixel als Vordergrund und unveränderte Pixel
# als Hintergrund beinhaltet. Wenn ihr euch das Bild nun
# anzeigen lasst, könnt ihr zwar die Positionen der
# Veränderungen selbst ermitteln und die Anzahl zählen,
# aber das soll nun ebenfalls der Computer machen.
skimage.io.imsave("bv.exercise.04.03.01-diff.png", diff)

# 3. Erweitert daher euer Skript, um die Funktionalität
# des Zählens der Veränderungen. Dabei ist jeder
# zusammenhängende Bereich an Pixeln, der sich verändert
# hat, als ein Bereich zu zählen.

img_copy = np.copy(diff)


# img_copy = np.array([[0, 1, 0], [1, 1, 1]])


def neighbors(inx: int, iny: int) -> []:
    start_x = max(inx - 1, 0)
    end_x = min(inx + 2, img_copy.shape[0])
    start_y = max(iny - 1, 0)
    end_y = min(iny + 2, img_copy.shape[1])
    coordinates = []

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            coordinates += [(x, y)]

    return coordinates


def prune_cluster(inx: int, iny: int) -> int:
    result = 0

    queue = neighbors(inx, iny)

    while len(queue) > 0:
        xy = queue.pop(0)

        # Neighbor Pixel is not part of the cluster
        # OR it is market as part of the cluster.
        if img_copy[xy] == 0 or img_copy[xy] == 0xff:
            continue

        result = 1
        img_copy[xy] = 0xff

        queue += neighbors(xy[0], xy[1])

    return result


prune_clusters = 0
for inx in range(diff.shape[0]):
    for iny in range(diff.shape[1]):
        prune_clusters += prune_cluster(inx, iny)

print("prune_clusters", prune_clusters)
skimage.io.imsave("bv.exercise.04.03.03.png", img_copy)
