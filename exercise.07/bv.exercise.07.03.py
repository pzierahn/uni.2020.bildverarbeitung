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

def apply_box_filter(n: int):
    box_filter = numpy.full((n, n), (1 / (n**2)))
    faltung = scipy.ndimage.convolve(rauschen, box_filter)
    skimage.io.imsave(f"bv.exercise.07.03.03.faltung.{n}.png", faltung)

apply_box_filter(3)
apply_box_filter(5)
apply_box_filter(7)
apply_box_filter(9)
apply_box_filter(11)