# module importieren
import csv

# funktion gibt anzahl geburten zurück
def anzahl_geburten(kreis, monat, jahr, kreis_liste, monat_liste, jahr_liste):

    # zähler mit 0 initiieren
    anzahl = 0

    # durch eine der listen iterieren
    for index,  aktueller_kreis in enumerate(kreis_liste):

        # aktueller monat und jahr
        aktueller_monat = monat_liste[index]
        aktuelles_jahr = jahr_liste[index]

        # filter
        if aktueller_kreis==kreis and aktueller_monat==monat and aktuelles_jahr==jahr:

            # zähler hochzählen
            anzahl = anzahl + 1

    # anzahl zurückgeben
    return anzahl

# datei öffnen
with open('geburten_zurich.csv') as csv_datei:

    # reader erstellen
    csv_reader = csv.reader(csv_datei, delimiter=';')

    # erste zeile "überspringen"
    next(csv_reader)

    # datenlisten vorbereiten
    kreise = []
    monate = []
    jahre = []

    # durch die zeilen iterieren
    for zeile in csv_reader:

        # relevante daten auslesen und konvertieren
        kreise.append(int(zeile[8]))
        monate.append(int(zeile[1]))
        jahre.append(int(zeile[0]))

# anzahl berechnen und ausgeben
print(anzahl_geburten(8, 5, 2023, kreise, monate, jahre))

