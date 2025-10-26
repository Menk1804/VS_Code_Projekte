

import os
import csv

# Pfad zur aktuellen Datei bestimmen
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'geburten_zurich.csv')

# Datei öffnen
with open(csv_path, encoding='utf-8') as csv_datei:
    csv_reader = csv.reader(csv_datei, delimiter=';')
    next(csv_reader)

    kreise = []
    monate = []
    jahre = []

    for zeile in csv_reader:
        kreise.append(int(zeile[8]))
        monate.append(int(zeile[1]))
        jahre.append(int(zeile[0]))

def anzahl_geburten(kreis, monat, jahr, kreis_liste, monat_liste, jahr_liste):
    anzahl = 0
    for index, aktueller_kreis in enumerate(kreis_liste):
        if (aktueller_kreis == kreis and
            monat_liste[index] == monat and
            jahr_liste[index] == jahr):
            anzahl += 1
    return anzahl

print(anzahl_geburten(8, 5, 2023, kreise, monate, jahre))
