import os
import math
import numpy
import skimage.io
import scipy.ndimage

# 1. Ladet zunächst das Bild einstein.png aus dem Moodle und verrauscht es mit
# Gaußschem Rauschen. Wandelt dafür zunächst den Wertebereich des Bildes von
# 0...255 auf 0...1 um. Nutzt zum Verrauschen entweder eure eigene Funktion
# von Aufgabenblatt 2 Aufgabe 5 oder nutzt die Funktion skimage.util.random_noise()
# mit dem Parameter mode=’gaussian’ und einer Varianz von 0.01. Zeigt das verrauschte Bild an.
img = numpy.array(skimage.io.imread("einstein.png"), numpy.uint8) / 0xff
skimage.io.imsave("bv.exercise.07.03.01.png", img)

rauschen = skimage.util.random_noise(img, mode="gaussian", var=0.01)
skimage.io.imsave("bv.exercise.07.03.01.rauschen.png", rauschen)


# 2. Schreibt eine Funktion, die den mittleren absoluten Unterschied zwischen den korrespondierenden
# Pixeln eines Bildes berechnet. Dazu müsst ihr durch alle Koordinaten der Bilder iterieren und
# jeweils die absolute Differenz der Pixelwerte beider Bilder an der entsprechenden Koordinate
# berechnen. Die Differenzen müssen schließlich aufsummiert und durch die Anzahl der Pixel geteilt
# werden. Wie groß ist die mittlere Differenz zwischen dem Originalbild (einstein.png) und eurer
# verrauschten Variante?
def mittler_absoluten_unterschied(img1: numpy.array, img2: numpy.array) -> float:
    diff = numpy.abs(img1 - img2)
    return float(numpy.mean(diff))


print("mittler_absoluten_unterschied", mittler_absoluten_unterschied(img, rauschen))


# 3. Wendet nun verschiedene Varianten eines Box-Filters auf das verrauschte Bild an. Die Varianten
# sollen sich in der Größe des n×n Filterkerns unterscheiden mit n ∈ {3, 5, 7, 9, 11}. Erstellt zunächst
# einen Filterkern entsprechender Größe und normiert diesen, sodass die Summe über den Filterkern
# 1 ist. Nutzt nun die Funktion scipy.ndimage.convolve(), um das Bild mit dem Filterkern
# zu falten. Evaluiert, welche Größe n zur geringsten mittleren Differenz zum Originalbild führt.
# Visualisiert zudem das beste Ergebnis.

def apply_box_filter(n: int) -> numpy.array:
    box_filter = numpy.full((n, n), (1 / (n ** 2)))
    faltung = scipy.ndimage.convolve(rauschen, box_filter)
    skimage.io.imsave(f"bv.exercise.07.03.03.faltung.{n}.png", faltung)

    return faltung


best_box_n = -1.0
best_box_diff = -1.0

for n in [3, 5, 7, 9, 11]:
    box_img = apply_box_filter(n)
    diff = mittler_absoluten_unterschied(img, box_img)

    if best_box_diff < 0 or best_box_diff > diff:
        best_box_n = n
        best_box_diff = diff

print("best_box_n", best_box_n)
print("best_box_diff", best_box_diff)


# 4. Wendet nun den Gauß-Filter mit unterschiedlichen Varianzen auf dasselbe verrauschte Bild an.
# Testet Varianzen im Bereich 0.1,...,2 in Schritten von 0.1 und vergleicht das Ergebnis erneut
# mit Hilfe der mittleren Differenz mit dem Originalbild. Welcher Filter liefert das bessere Ergebnis
# (geringere mittlere Differenz zum Originalbild)? Visualisiert zudem das beste Ergebnis mit dem
# Gauß-Filter. Sieht man einen Unterschied im Vergleich zum besten Ergebnis des Box-Filters?

def apply_gauss_filter(n: int, sig: float) -> numpy.array:
    gauss_filter = numpy.zeros((n, n))

    dir = "bv.exercise.07.03.04.gauss"
    os.makedirs(dir, exist_ok=True)

    center = math.floor(n / 2)

    for nx in range(n):
        for ny in range(n):
            r = math.sqrt((nx - center) ** 2 + (ny - center) ** 2)
            gauss_filter[nx][ny] = math.exp(-((r ** 2) / (2 * sig ** 2)))

    # print("gauss_filter")
    # print(gauss_filter)

    faltung = scipy.ndimage.convolve(rauschen, gauss_filter)
    # skimage.io.imsave(f"{dir}/{n}x{n}-{sig}.png", faltung)

    return faltung


best_n = -1.0
best_sig = -1.0
best_diff = -1.0

for n in [3, 5, 7, 9, 11]:
    for inx in range(1, 21):
        sig = inx * 0.1
        gauss_img = apply_gauss_filter(n, sig)
        diff = mittler_absoluten_unterschied(img, gauss_img)

        if best_diff < 0 or best_diff > diff:
            best_n = n
            best_sig = sig
            best_diff = diff

        # print("sig", sig)
        # print("diff", diff)
        # break

print("best_n", best_n)
print("best_sig", best_sig)
print("best_diff", best_diff)
