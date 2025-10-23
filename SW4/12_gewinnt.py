import random

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Willkommen zu 12 GEWINNT")
print("Du beginnst...")

summe_spielerin = 0
weitermachen = True

while weitermachen:
    print(f'Deine Summe ist "{summe_spielerin}"')
    antowrt = input('Soll eine weitere Zahl gezogen werden? (j=ja, n=Nein) :')

    if antowrt == 'j':
        neue_zahl = random.randint (1, 4)
        print(f'Es wurde eine "{neue_zahl}" gezogen')

        summe_spielerin = summe_spielerin + neue_zahl
        if summe_spielerin == 12:
            print("GEWONNEN! - Du hast genau '12' erreicht")
            break
        if summe_spielerin > 12:
            print("Leider verloren - Deine Summe ist grösser als '12'")
            break
    else:
        weitermachen = False

if(not weitermachen):
    print("Das Programm versucht dich jetzt zu schlagen...")

    summe_programm = 0
    while summe_programm <= summe_spielerin:
        print(f'Die Summe der Programms ist "{summe_programm}"')

        neue_zahl = random.randint(1, 4)
        print(f'Das Programm zieht eine "{neue_zahl}"')

        summe_programm = summe_programm + neue_zahl
        if summe_programm >12:
            print('GEWONNEN! - Das Programm hat eine Summe die grösser als "12" ist.')
            break
        if summe_programm > summe_spielerin:
            print(f'Leider verloren! - "{summe_programm}" ist grösser als "{summe_spielerin}"')
            break

print("Vielen Dank fürs Mitmachen - hat Spasss gemacht!")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")



