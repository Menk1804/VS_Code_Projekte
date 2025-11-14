int_var = 42
float_var = 3.14

produkt = int_var * float_var
print(f'Wert {produkt} | Datentyp: {type(produkt)}')
hoch_3 = int_var ** 3
print(f'Wert: {hoch_3} | Datentyp: {type(hoch_3)}')
int_div = int_var // 4
print(f'Wert: {int_div} | Datentyp: {type(int_div)}')
float_rest = float_var % 3
print(f'Wert: {float_rest} | Datentyp: {type(float_rest)}')

str_var = str(float_var) + 'ist ungefähr die Kreiszahl Pi'
print(str_var)
neuer_text = str_var.replace('ungefähr die', 'die gerundete')
print(neuer_text)

fibonacci_list = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fibonacci_list)
fibonacci_list.append(1)
print(fibonacci_list)
fibonacci_list.sort()
print(fibonacci_list)

farben = {'weiss' :[255, 255, 255], 'rot' :[255, 0, 0]}
farben['violett'] = [180, 0, 255]
print(farben)

print(f"Violett hat die RGB-Kodierung {farben['violett']}")
print(f"Der Rotanteil von Violett ist {farben['violett'][0]}")
