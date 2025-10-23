# variablen definieren
messwerte = [21.4, 21.5, 20.8, 20.4, 19.9]
schwellwerte = (20, 21.4)

# überprüfung ob die messwerte im akzeptablen Bereich sind.
# Code Funktionier noch nicht
ist_akzeptable = messwerte[0] >= schwellwerte[0] and messwerte[1] >= schwellwerte[1] and messwerte[2] >= schwellwerte[2]
if ist_akzeptable:
    print('alles in Ordnung')
