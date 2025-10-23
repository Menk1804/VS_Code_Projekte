grenzwert = 5

# # Zahl von User abfragen
# eingabe = input('Bitte gib eine Zahl zwischen 1 und 10 ein: ')
# zahl = float(eingabe)

#Zufällige Eingabe erzeugen
import random
eingabe = random.randint(1,10)


#Überprüfen der Eingabe
bedingung = grenzwert < eingabe
if bedingung:
    print(f'Die Zufallszahl {eingabe} ist grösser als der Grenzwert')
else:
    print(f'Die Zufallszahl {eingabe} ist kleiner oder gleich gross wie der Grenzwert')   





