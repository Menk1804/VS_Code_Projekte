#Fragt den Benutzer nach dem Gewicht.

gewicht = float(input('Wie schwer sind Sie in kg?'))
print(gewicht)

#Fragt den Benutzer nach der Körpergrosse in Meter

groesse = float(input('Wie gross sind sie in m?'))
print(groesse)

#Berechnung des BMI

bmi = gewicht / (groesse ** 2)


print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi:.2f} kg/m²")



# # BMI-Berechnung in Python

# # Benutzer nach Gewicht fragen
# gewicht = float(input("Bitte geben Sie Ihr Körpergewicht in Kilogramm ein: "))

# # Benutzer nach Körpergröße fragen
# groesse = float(input("Bitte geben Sie Ihre Körpergröße in Metern ein: "))

# # BMI berechnen (Formel: Gewicht / Größe²)
# bmi = gewicht / (groesse ** 2)

# # Ergebnis ausgeben
# print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi:.2f} kg/m²")
