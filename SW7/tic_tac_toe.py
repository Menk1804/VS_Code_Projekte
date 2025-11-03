import random

startfelder = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def spielfeld_anzeigen(felder):

    print('')
    print('-------------')
    print(f'| {felder[0]} | {felder[1]} | {felder[2]} |')
    print('-------------')
    print(f'| {felder[3]} | {felder[4]} | {felder[5]} |')
    print('-------------')
    print(f'| {felder[6]} | {felder[7]} | {felder[8]} |')
    print('-------------')
    print('')


def spielfeld_auswerten(felder):

    # testen, ob [g]ewonnen
    # reihen
    if felder[0]==felder[1] and felder[1]==felder[2]:
       return 'g'
    if felder[3]==felder[4] and felder[4]==felder[5]:
       return 'g'
    if felder[6]==felder[7] and felder[7]==felder[8]:
       return 'g'
    # spalten
    if felder[0]==felder[3] and felder[3]==felder[6]:
       return 'g'
    if felder[1]==felder[4] and felder[4]==felder[7]:
       return 'g'
    if felder[2]==felder[5] and felder[5]==felder[8]:
       return 'g'
    # diagonalen
    if felder[0]==felder[4] and felder[4]==felder[8]:
       return 'g'
    if felder[2]==felder[4] and felder[4]==felder[6]:
       return 'g'

    # testen, ob [u]nentschieden oder [w]eiter
    for feld in felder:
        if feld in startfelder:
           return 'w'
    return 'u'


def spielzug():

    while True:

        # eingabe im terminal
        eingabe = input('Bitte Feld eingeben: ')

        # abbruch
        if eingabe=='a':
            return eingabe

        # feldeingabe testen
        if eingabe in startfelder:
            if spielfelder[int(eingabe)-1] in ['X', 'O']:
                print('Das Feld ist schon besetzt')
            else:
               return eingabe
        else:
            print('"' + eingabe + '" ist keine gültige Eingabe')


def ai(felder):

    # noch freie felder bestimmen
    freie_felder = []
    for feld in felder:
        if feld in startfelder:
            freie_felder.append(feld)

    # zufälliger zug
    return random.choice(freie_felder)


# spiel starten
print('')
print('-------------------------------------------')
print('WILLKOMMEN zu TIC TAC TOE')
print('-------------------------------------------')
print('Eingaben:')
print('  - Spielzug: wähle freies Feld [1] bis [9]')
print('  - Spiel abbrechen: [a]brechen')
print('-------------------------------------------')

# spielfelder mit startfeldern initialisieren
spielfelder = startfelder.copy()
spielfeld_anzeigen(spielfelder)

# spiel schleife
while True:

    # spieler:in ist an der reihe
    eingabe = spielzug()

    # abbruch
    if eingabe=='a':
        print('Spiel abgebrochen - Bis bald!')
        print('')
        break

    # eingabe ins feld und spielfeld anzeigen
    spielfelder[int(eingabe)-1] = 'X'
    spielfeld_anzeigen(spielfelder)

    # spielfeld auswerten
    status = spielfeld_auswerten(spielfelder)
    if status=='g':
        print('GRATULATION - du hast gewonnen!')
        print('')
        break
    elif status=='u':
        print('Unentschieden - gut gemacht!')
        print('')
        break

    # computer ist an der reihe
    eingabe = ai(spielfelder)
    print('Die KI gibt Feld ' + eingabe + " ein.")

    # eingabe ins feld und spielfeld anzeigen
    spielfelder[int(eingabe)-1] = 'O'
    spielfeld_anzeigen(spielfelder)

    # spielfeld auswerten
    status = spielfeld_auswerten(spielfelder)
    if status=='g':
        print('Ach Mist! Die KI hat gewonnen.')
        print('')
        break
    elif status=='u':
        print('Unentschieden - probiers nochmal!')
        print('')
        break
