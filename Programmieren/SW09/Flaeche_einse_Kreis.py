# Importiert die Module für die Berechnungen
import random as rnd
from math import pi, sqrt as sr

# Erzeugt einen Zufälligen Radius zwischen 1-10

n = rnd.randint(1,10) #ganze Zahl zwischen 1 und 10
radius = n ** 2  # Quadriert den Radius

#Formel für die Kreisfläche
circle_area = pi * radius ** 2

#Seitenlänge des Dreicks berechnen
side_length = sr(4 * circle_area / sr(3))

# Höhe des Dreiecks berechnen
hight = side_length * sr(3) / 2

# Ausgabe der Ergebnisse im Terminal
print("Zufälliger Radius des Kreises:", radius)
print("Seitenlänge des gleichseitigen Dreiecks:", side_length)
print("Höhe des gleichseitigen Dreiecks:", hight)

