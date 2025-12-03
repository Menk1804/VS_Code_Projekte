# Importiert die Math Bibliothek
import math
import random as rnd

# Funktionen für die Berechnung erstellen

def random_radius():
    """Erzeugt einen Zufallsradius als Quadrat einer Zahl zwischen 1 und 10."""
    n = rnd.randint(1, 10)
    return n ** 2

def circle_area(radius):
    """Berechnet die Fläche eines Kreises mit gegebenem Radius."""
    return math.pi * radius ** 2

def triangle_side_for_area(area):
    """Berechnet die Seitenlänge eines glechseitigen Dreiecks für eine gegebene Fläche."""
    return math.sqrt(4 * area / math.sqrt(3))

def triangle_height(side_length):
    """Berechnet die Höhe eines gleichseitigen Dreiecks aus der Seitenlänge."""
    return side_length * math.sqrt(3) / 2


# Diese Funktion verdindet die obigen Funktionen

def run_calculation_once():
    """Fürht eine kompletten Berechnungsdurchlauf aus und bigt RAdius, Seitenlänge und Höhe zurück"""
    radius = random_radius()
    area = circle_area(radius)
    side = triangle_side_for_area(area)
    height = triangle_height(side)
    return radius, side, height

#Ausgebe der Funktion ist separat von der Lokik
def print_result(radius, side, height):
    """Gibt die Resultate formatiert aus."""
    print("Zufälliger RAdius des Kreises:", radius)
    print("Seitenlänge des gleichseitigen Dreiecks:", side)
    print("Höhe des gleichseitigen Dreiecks:", height)
    print() # Gibt eine Leerezeile im Terminal aus für bessere übersicht.


#Ist dafür, dass die Berechnungen nur ausgeführt werden, wenn das Script gestarted wird.
