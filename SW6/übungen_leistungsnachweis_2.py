#übung mit while schleiffe

# zahl = 2

# while zahl <=12:
#     print(zahl + 2)

# zahl = 1

# while zahl <= 5:
#     print("Aktuelle Zahl:", zahl)
#     zahl = zahl + 1  # oder: zahl += 1


# for i in range(3):
#     print(f'Die zahle wurde um einz erhöt {zahl + 1}')

#übung mit Funktionen
# def mein_name():
#     print("Mein name ist Menk")


# mein_name()

#Prüft, ob die Blutgruppe kompatible ist

def ist_kompatible(empfangende_bg, spendende_bg):
    kompatibiliteat = {
        "AB+": ["0-", "0+", "B-", "B+", "A-", "A+", "AB-", "AB+"],
        "AB-": ["0-", "B-", "A-", "AB-"],
        "A+" : ["0-", "0+", "A-", "A+"],
        "A-" : ["0-", "A-"],
        "B+" : ["0-", "0+", "B-", "B+"],
        "B-" : ["0-", "B-"],
        "O+" : ["0-", "0+"],
        "O-" : ["0-"]
    }
    kompatibiliteat = spendende_bg in kompatibiliteat[empfangende_bg]
    return kompatibiliteat

#blutgruppe der empfänger Fragen
empfangende_bg = input("Welche Blutgruppe hat der Empfänger?")

#blutgruppe der spender erfragen
spendende_bg = input("Welche Blutgruppe hat der Spender?")

#Kompatibilität prüfen
if ist_kompatible(empfangende_bg, spendende_bg):
    print("Die Spende ist kompatible")
else:
    print("Die Spende ist nicht kompatible")


# datei = open("geburten_zurich.csv")

# print(datei)

# def vorname_nachnme(vorname, nachname):
#     return vorname +''+ nachname

# name = vorname_nachnme("Menk", "vonWeissenfluh")

# print(name)


# def begruessung():
#     print("Hallo")


# begruessung()


# def begruessung_name(name):
#     print("Hallo", name + "!")

# begruessung_name("Menk")
# begruessung_name("Afra")
# begruessung_name("Max")

# def begruessung_stadt(name)

# def begruessung_stadt(name, stadt):
#     print("Hallo", name, "aus", stadt + "!")

# begruessung_stadt("Menk", "Meiringen")
# begruessung_stadt("Lara", "Bern")

# #Zahlen addieren
# def addieren(a, b, c):
#     ergebnisse = a + b + c
#     print(ergebnisse)
#     return ergebnisse

# addieren(1, 2, 3)

# def farbe_und_zahl():
#     return "blau", 7

# farbe, zahl = farbe_und_zahl()
# print("Farbe:", farbe)
# print("Zahl:", zahl)

# def quadrat(x):
#     return x * x



# def summe_der_quadrate(a, b):
#     return quadrat(a) + quadrat(b)

# ergebnisse = summe_der_quadrate(2,3)
# print(ergebnisse)

# def durchschnitt(v1, v2, v3):
#     wert = (v1 + v2 + v3) / 3
#     print(wert)
#     return wert

# durchschnitt(5, 10, 15)
# durchschnitt(2, 4, 3)

# def celsius_in_fahrenheit(c):
#     return c * 9/5 + 32

# temp_c = float(input("Temperatur in °C:"))
# temp_f = celsius_in_fahrenheit(temp_c)
# print(f"Das sind {temp_f} °F")

# def anzahl_zeichen(text):
#     anzahl_buchstaben = len(text)
#     anzahl_worter = len(text.split())
#     return anzahl_buchstaben, anzahl_worter

# text = input("Gib einen Text ein:")
# zeichen, worter = anzahl_zeichen(text)
# print(f"Zeichen: {zeichen}")
# print(f"Wörter {worter}")

# for l in range(5):
#     print(l)

# for i in range(2, 11, 2):
#     print(i)

# namen = ["Anna", "Ben", "Clara"]

# for namen in namen:
#     print(f"Hallo {namen}")

# tiere = ["Hund", "Katze", "Maus"]

# for i in range(len(tiere)):
#     print(f"{tiere[i]} ist an Position {i}")

# tiere = ["Hund", "Katze", "Maus"]

# for index, tier in enumerate(tiere):
#     print(index, tier)

# while True:
#     wort = input("Wort eingeben ('stop' zum Beenden): ")
#     if wort == "stop":
#         print("Du hast das Programm gestopt!")
#         break
#     print("Du hast eingegeben:", wort)

# for i in range (1, 11):
#     if i % 2 != 0:
#         continue
#     print(i)

# anzahl = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         anzahl += 1
# print(F"Es gibt {anzahl} gerader Zahlen.")

# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print(i)

# summe = 0

# for i in range(1, 101):
#     summe += i

# print("Summe:", summe)

# woerter = ["Apfel", "Schokolade", "Haus", "Programmieren", "Brot"]

# for wort in woerter:
#     if len(wort) <= 5:
#         continue
#     print(wort)

