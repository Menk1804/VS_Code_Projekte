# meine_variable = 0

# try:
#     resultat = 100 / meine_variable
# except Exception as e:
#     print(str(e))
#     resultat = 100
#     ('Ausnahme!')

# print(resultat)


#Neue code bespiele obriger code ist auskommentiert


# begrüssung funktion
def welchome(nutzername, botschaft):
    print(f'Hallo {nutzername}')
    if botschaft== 1:
        print("Schön, dass du da bist. Gleich geht's los")
    elif botschaft==2:
        print("Ich freue mich, dass du dabei bist.")
    elif botschaft== 3:
        print("Grossartig, Ich freue mich")
    else:
        print("Schön, dass du da bist. Gleich geht's los")








# frage nach dem namen des ersten benutzers
name = input("Wie heisst du? :")
welchome(botschaft=1, nutzername=name)

# frage nach dem namen des zweiten benutzers
name = input("Wie heisst du? :")
welchome(name, 2)

# frage nach dem namen dritten benutzers
name = input("Wie heisst du? :")
welchome(name, 3)


