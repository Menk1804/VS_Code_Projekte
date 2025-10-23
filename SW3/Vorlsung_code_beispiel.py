

# ph_wert = float(input('Wie hoch ist der PH-Wert?'))

# if(ph_wert<0):
#     print('Du hast einen ungültigen Wert eingegeben')

# elif(ph_wert<4):
#     print('stark sauer')
# elif(ph_wert<6):
#     print('sauer')
# elif(ph_wert<9):
#     print('Neutral')
# elif(ph_wert<11):
#     print('Alkalisch')
# elif(ph_wert<=14):
#     print('stark Alkalisch')
# elif(ph_wert>14):
#     print('Der Wert ist ungültig')


# alter = int(input('Wie alt bist du?'))
# print(alter)

# rechnung = alter / 3
# print(f'{rechnung:.2f}')


# #Fragt den Nutzer nach einer Zahl
# zahl = int(input('Eine Zahle zwischen 1 bis 10'))
# print(zahl)

# #Prüft ob 4 in test ist
# test = [1, 2, 3, 5, 6, 7, 8, ]
# ist_die_zahl = zahl in test


# print(ist_die_zahl)

# a = ('Hallo')
# b = ('ich')
# c = ('bin')
# d = ('22 Jahre alt.')

# print(f'{a}  {b}  {c}  {d}')


# s = 'Hi'

# print(s * 3)

#Fragt den Nutzer nach dem pH-Wert


# pH_wert = int(input('Wie gross ist der pH-Wert'))
# print(pH_wert)

# if pH_wert<0 or pH_wert>14:
#     print(f'Der Wert {pH_wert} ist nicht im definirten Bereich')
# elif pH_wert<4:
#     print('Stark sauer')
# elif pH_wert<6:
#     print('Sauer')
# elif pH_wert<9:
#     print('Neutral')
# elif pH_wert<11:
#     print('Alkalisch')
# elif pH_wert<=14:
#     print('Stark alkalisch')



# pH_wert = int(input('Wie gross ist der pH-Wert?'))

# if pH_wert < 0 or pH_wert > 14:
#     print('Ungültiger Wert')
# elif pH_wert < 4:
#     print('Stark sauer')
# elif pH_wert < 6:
#     print('Sauer')
# elif pH_wert < 9:
#     print('Neutral')
# elif pH_wert < 11:
#     print('Alkalisch')
# elif pH_wert <= 14:
#     print('Stark alkalisch')


# werte = ('Ich heisse Menk')

# test = werte.split('s')

# print(test)


dictionary = { 'Menk' : '22',
              'Sharon' : '23',
              'Afra': '25',
              'Max' : '18',
              }

auswertung = dictionary.values()
print(auswertung)
