# antworten definieren
antworten = ["ja", "nein"]

# frage 1 gemäss entscheidungsschema
antwort = input(f'''Möchten Sie ein Nickerchen machen?
Antworten Sie bitte mit "{antworten[0]}" oder "{antworten[1]}" : ''')

# testen, ob antwort "verständlich"
if(antwort not in antworten):
    print('Ihre Antwort ist leider unverständlich')

# ja oder nein?
if(antwort==antworten[0]):

    # frage 2 gemäss entscheidungsschema
    antwort = input(f'''Ist es schon nach 16 Uhr?
    Antworten Sie bitte mit "{antworten[0]}" oder "{antworten[1]}" : ''')

    # testen, ob antwort "verständlich"
    if(antwort not in antworten):
        print('Ihre Antwort ist leider unverständlich')

    # ja oder nein?
    if(antwort==antworten[0]):

        # frage 3 gemäss entscheidungsschema
        antwort = input(f'''Haben Sie 30 Minuten Zeit?
        Antworten Sie bitte mit "{antworten[0]}" oder "{antworten[1]}" : ''')

        # testen, ob antwort "verständlich"
        if(antwort not in antworten):
            print('Ihre Antwort ist leider unverständlich')

        # ja oder nein?
        if(antwort==antworten[0]):
            print('Machen Sie ein Nickerchen')
        else:
            print('Machen Sie kein Nickerchen')

    else:
        print('Machen Sie kein Nickerchen')

else:
    print('Machen Sie kein Nickerchen')
