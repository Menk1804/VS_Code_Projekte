gewicht = float(input('Wie schwer bist?'))
groesse = float(input('Wie gross bist du?'))

#Berechnung BMI

bmi = gewicht / (groesse ** 2 )
print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi:.2f} kg/m²")

 