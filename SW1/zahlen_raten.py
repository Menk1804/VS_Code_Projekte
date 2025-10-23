import random
gedachte_zahl = random.randint(1, 10) 

erraten = False
while(not erraten):
    zahl = input('An welche Zahle zwischen 1 und 10 denke ich?')
    zahl = int(zahl)

    if(zahl > gedachte_zahl):
        print('Meine gedachte Zahl ist kleiner.')

    if(zahl< gedachte_zahl):
        print('Meine gedachte Zahl ist grösser.')   

    if(zahl == gedachte_zahl):
        print('Gratulation! Du hast meine Zahl erraten!')
        erraten = True

