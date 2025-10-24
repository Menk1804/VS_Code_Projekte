

import csv
import os

# Bestimme automatisch den Pfad zur CSV-Datei im gleichen Ordner wie das Skript
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'saturation_per_day.csv')

# Öffne die CSV-Datei und lese sie Zeile für Zeile ein
with open(file_path, newline='', encoding='utf-8') as csv_datei:
    csv_reader = csv.reader(csv_datei)
    for zeile in csv_reader:
        print(zeile)
