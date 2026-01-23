# Fragt den Benutzer nach der Körpergrösse.
groesse = float(input("Wie gross sind sie in m ?"))

#Fragt den Benutzer nach dem Hüfftumfang
hueftumfang = float(input("Wie gross ist ihr Hüfftumfang in cm ?"))

#Fragt den Benutzer nach dem Geschlecht
geschlecht = (input("welches Geschlecht haben sie m oder w ?"))

#Fragt nach dem Alter
alter = int(input("Wie alt sind sie?"))


# Berechnet den BAI
if geschlecht == "m":
    BAI = hueftumfang/(groesse**1.5) - 6
else:
    BAI = hueftumfang/(groesse**1.5) - 18



if alter < 40:
    if BAI <21:
        print("untergewichtig")
    elif BAI <33:
        print("gesund")
    elif BAI <39:
        print("übergewichtig")
    else:
        print("adipös")
elif alter <60:
    if BAI <23:
        print("untergewichtig")
    elif BAI <35:
        print("gesund")
    elif BAI <41:
        print("übergewichtig")
    else:
        print("adipös")
else:
    if BAI <25:
        print("untergewichtig")
    elif BAI <38:
        print("gesund")
    elif BAI <43:
        print("übergewichtig")
    else:
        print("adipös")
