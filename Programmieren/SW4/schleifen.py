# import von modulen
import random

# liste der blutsauerstoff-sättigung pro tag
blutsauerstoff_sättigung = []
for tag in range(0, 365):
    blutsauerstoff_sättigung.append(random.random()*12+88)

# Aufgabe 1
tag = 0
while tag <365:
    if(blutsauerstoff_sättigung[tag]<90):
        break
    else:
        tag = tag + 1
print(f'Erster Tag, an dem der Wert unter 90 fiel: {tag}')


# Aufgabe 2
tage = []
for tag, wert in enumerate(blutsauerstoff_sättigung):
    if(wert<90):
        tage.append(tag)
print(f'Tage mit einem Wert unter 90: {len(tage)}')


