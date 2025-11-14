#Frage den Benutzer was er berechnen will.
Bmi_RFM = input("Was möchten du berechnen den BMI oder RFM?")

if Bmi_RFM=="BMI":
    gewicht = float(input('Wie schwer bist?'))
    groesse = float(input('Wie gross bist du?'))

    #Berechnung BMI

    bmi = gewicht / (groesse ** 2 )
    print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi:.2f} kg/m²")

elif Bmi_RFM == "RFM":

    #Fragt den Benutzer nach dem Geschlecht 

    geschlecht = input('Sind sie w oder m?')

    #Frage nach der Koerpergroesse
    groesse = float(input('Wie gross sind sie in cm?'))

    #Frage den Benutzer nach dem Hueftumfang
    hueftumfang = float(input('Wie gross ist ihr Hüftunfang in cm?'))

    #Berechnet den RFM für Frauen
    if geschlecht == 'w':
        rfm_berechnung_w = 76 - (20 * (groesse/hueftumfang))
        print(f'{rfm_berechnung_w:.2f}%')

        if rfm_berechnung_w <10:
            print('Äusserst geringer Fettgehalt')
        elif rfm_berechnung_w <13:
            print('Essenzieller Fettgehalt')
        elif rfm_berechnung_w <20:
            print('Athletischer Fettgehalt')
        elif rfm_berechnung_w <24:
            print('Trainierter Fettgehalt')
        elif rfm_berechnung_w <31:
            print('Durchschnittlicher Fettgehalt')
        else:
            print('Übergewichtiger Fettgehalt')

    
    


 #Berechnet den RFM für Männer   
    else:
        rfm_berechnung_m = 64 - (20 * (groesse/hueftumfang))
        print(f'{rfm_berechnung_m:.2f}%')

        if rfm_berechnung_m <2:
            print('Äusserst geringer Fettgehalt')
        elif rfm_berechnung_m <5:
            print('Essenzieller Fettgehalt')
        elif rfm_berechnung_m <13:
            print('Athletischer Fettgehalt')
        elif rfm_berechnung_m <17:
            print('Trainierter Fettgehalt')
        elif rfm_berechnung_m <24:
            print('Durchschnittlicher Fettgehalt')
        else:
            print('Übergewichtiger Fettgehalt')

#Fals keine Gültige Angabe
else:
    print("Sie haben leider keine Gültige eingabe gemacht.")
