# module importieren
import random

# schere, stein, papier anzeigen
def anzeigen(wahl, invers=False):

    # ---------------------------
    # schere
    if wahl==1:
        if invers:
            print('''
       _______
  ____(____   '---
 (______
(__________
      (____)
       (___)__.---
''')
        else:
            print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    # ---------------------------
    # stein
    elif wahl==2:
        if invers:
            print('''
  _______
 (____   '---
(_____)
(_____)
 (____)
  (___)__.---
''')
        else:
            print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    # ---------------------------
    # papier
    elif wahl==3:
        if invers:
            print('''
      _______
 ____(____   '---
(______
(_______
 (_______
  (__________.---
''')
        else:
            print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
    else:
        print('''Ungültige Eingabe''')

#==================================
#=== Hier beginnt die Challenge ===
#==================================
# auswahl
auswahl = ['SCHERE', 'STEIN', 'PAPIER']

# start
print('')
print('''=================================''')
print('''   SCHERE <-> STEIN <-> PAPIER   ''')
print('''=================================''')
print('')

# frage nach der benötigten anzahl punkte für den sieg
print('Auf wieviele Siegpunkte soll gespielt werden?')
sieg_punkte = int(input('Bitte eine ganze Zahl eingeben (z.B. 5) : '))

# initialisierung der punkte
punkte_spielerin = 0
punkte_computer  = 0

# auswertung
def auswertung(wahl_1, wahl_2):

    # vergleich
    if wahl_1==wahl_2:
        print('==> Unentschieden')
        return 0, 0
    elif wahl_1==1 and wahl_2==3:
        print('==> Du hast diese Runde gewonnen!')
        return 1, 0
    elif wahl_1==2 and wahl_2==1:
        print('==> Du hast diese Runde gewonnen!')
        return 1, 0
    elif wahl_1==3 and wahl_2==2:
        print('==> Du hast diese Runde gewonnen!')
        return 1, 0
    else:
        print('==> Diese Runde geht an den Computer')
        return 0, 1

# spiel schleife
while True:

    # zug spieler:in
    print('''Bitte wähle:
  - Schere: 1
  - Stein : 2
  - Papier: 3''')
    wahl_spielerin = int(input('Deine Wahl: '))
    print(f'''Du hast {auswahl[wahl_spielerin-1]} gewählt:''')
    anzeigen(wahl_spielerin)

    # zug computer
    wahl_computer = random.choice([1, 2, 3])
    print(f'''Der Computer hat {auswahl[wahl_computer-1]} gewählt:''')
    anzeigen(wahl_computer, True)

    # runde auswerten
    punkt_spielerin, punkt_computer = auswertung(wahl_spielerin, wahl_computer)
    punkte_spielerin = punkte_spielerin + punkt_spielerin
    punkte_computer = punkte_computer + punkt_computer

    # aktuellen zwischenstand anzeigen
    print(' -------------------------')
    print('| Aktueller Zwischenstand |')
    print(f'''|  Du: {punkte_spielerin}  |  Computer: {punkte_computer}  |''')
    print(' -------------------------')
    print('')

    # spiel fertig?
    if punkte_spielerin>=sieg_punkte:
        print('================================')
        print(' GRATULATION - Du hast gewonnen!')
        print('================================')
        print('')
        break
    if punkte_computer>=sieg_punkte:
        print('=======================================')
        print(' Ah, Mist! - Der Computer hat gewonnen!')
        print('=======================================')
        print('')
        break


