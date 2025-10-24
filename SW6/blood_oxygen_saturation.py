


import csv
import os

# Funktion: Gibt alle Tage zurück, an denen der Wert unter einem bestimmten Schwellenwert liegt
def days_below_threshold(threshold, days, values):
    critical_days = []
    for index, value in enumerate(values):
        if value < threshold:
            critical_days.append(days[index])
    return critical_days


# Automatisch den korrekten Pfad zur CSV-Datei ermitteln
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'saturation_per_day.csv')

# CSV-Datei einlesen
with open(file_path, newline='', encoding='utf-8') as csv_datei:
    csv_reader = csv.reader(csv_datei, delimiter=';')
    dates = []
    saturation = []

    # Überspringt die erste Zeile (Kopfzeile)
    next(csv_reader)

    # Jede Zeile einlesen
    for zeile in csv_reader:
        if len(zeile) >= 2:  # prüft, ob genug Spalten vorhanden sind
            dates.append(zeile[0])
            saturation.append(float(zeile[1]))

# Ausgabe aller Tage mit Sättigung unter 90
critical = days_below_threshold(90, dates, saturation)
print("Tage mit Sättigung unter 90%:")
print(critical)
