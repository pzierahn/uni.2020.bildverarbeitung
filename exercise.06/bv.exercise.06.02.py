import time
import numpy
import skimage.io


# 1. Schreibt zunächst eine Funktion, welche die Varianz nach Formel 1 in zwei Durchläufen durch
# das Bild berechnet. Im ersten Durchlauf soll dabei der Mittelwert μI berechnet werden und im
# zweiten Durchlauf schließlich die Varianz. Nutzt dazu unbedingt zwei verschachtelte for-Schleifen
# pro Durchlauf, um über die Pixel zu iterieren, und nutzt zur Berechnung keine Funktionen wie
# np.mean() oder np.var(). Testet eure Funktion an dem bekannten Testbild mandrill.png aus
# dem Moodle.
def formel_1(bild: numpy.array) -> (float, float):
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

    return standard_deviation, mean


# 2. Implementiert nun eine Funktion für die Varianzberechnung in einem Durchlauf nach Formel 2.
# Nutzt dazu erneut unbedingt zwei verschachtelte for-Schleifen pro Durchlauf, um über die Pixel
# zu iterieren, und nutzt zur Berechnung erneut keine Funktionen wie np.mean() oder np.var().
# Testet eure Funktion wieder am Testbild mandrill.png.
def formel_2(bild: numpy.array) -> (float, float):
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

    return standard_deviation, mean

# 3. Vergleicht nun eure Implementationen im Hinblick auf
# das Ergebnis und auf die Ausführungszeit.
# Findet und notiert eine Erklärung,
# warum die Ergebnisse leicht voneinander abweichen.
# Zum Ver- gleich der Ausführungszeiten soll je Funktion
# 10 mal die Varianz auf dem Testbild mandrill.png
# berechnet werden. Für die Zeitmessung solltet
# ihr auf die Funktion time.time(), die auf dem
# Aufgabenblatt 1 beschrieben wurde, zurückgreifen.
def time_test(bild: numpy.array):
    start = time.time()
    for _ in range(10):
        formel_1(bild)

    end = time.time()
    print("elapsed time formel_1", (end - start))

    start = time.time()
    for _ in range(10):
        formel_2(bild)

    end = time.time()
    print("elapsed time formel_2", (end - start))


bild = skimage.io.imread("mandrill.png")
time_test(bild)

# standard_deviation, mean = formel_1(bild)
# print("Formel 1")
# print("mean", mean)
# print("standard_deviation", standard_deviation)

# standard_deviation, mean = formel_2(bild)
# print("Formel 2")
# print("mean", mean)
# print("standard_deviation", standard_deviation)
