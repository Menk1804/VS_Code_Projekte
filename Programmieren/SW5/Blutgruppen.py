# funktion zur bestimmung der kompatibilität
def ist_kompatible(empfangende_bg, spendende_bg):
    kompatibilitaet_matrix = {
        "AB+": ["0-", "0+", "B-", "B+", "A-", "A+", "AB-", "AB+"],
        "AB-": ["0-", "B-", "A-", "AB-"],
        "A+" : ["0-", "0+", "A-", "A+"],
        "A-" : ["0-", "A-"],
        "B+" : ["0-", "0+", "B-", "B+"],
        "B-" : ["0-", "B-"],
        "O+" : ["0-", "0+"],
        "O-" : ["0-"]
    }
    kompatibel = spendende_bg in kompatibilitaet_matrix[empfangende_bg]
    return kompatibel

# blutgruppe der empfänger erfragen
empfangende_bg = input('Welche Blutgruppe hat der Empfänger?:')

#blutgruppe der spender erfragen
spendende_bg = input('Welche Blutgruppe hat die Spender:in? : ')

# kompatibilität prüfen
if ist_kompatible(empfangende_bg, spendende_bg):
    print('Die Spende ist kompatibel')
else:
    print('Die Spende ist nicht kompatibel')
