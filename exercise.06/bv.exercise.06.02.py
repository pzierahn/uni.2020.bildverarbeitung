import numpy
import skimage.io


# 1. Schreibt zunächst eine Funktion, welche die Varianz nach Formel 1 in zwei Durchläufen durch
# das Bild berechnet. Im ersten Durchlauf soll dabei der Mittelwert μI berechnet werden und im
# zweiten Durchlauf schließlich die Varianz. Nutzt dazu unbedingt zwei verschachtelte for-Schleifen
# pro Durchlauf, um über die Pixel zu iterieren, und nutzt zur Berechnung keine Funktionen wie
# np.mean() oder np.var(). Testet eure Funktion an dem bekannten Testbild mandrill.png aus
# dem Moodle.
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


# 2. Implementiert nun eine Funktion für die Varianzberechnung in einem Durchlauf nach Formel 2.
# Nutzt dazu erneut unbedingt zwei verschachtelte for-Schleifen pro Durchlauf, um über die Pixel
# zu iterieren, und nutzt zur Berechnung erneut keine Funktionen wie np.mean() oder np.var().
# Testet eure Funktion wieder am Testbild mandrill.png.
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
