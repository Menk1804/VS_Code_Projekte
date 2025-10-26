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