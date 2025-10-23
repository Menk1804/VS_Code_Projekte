# gegebene variablen
zauberlehrling = '''Walle! walle
                    Manche Strecke,
                    daß, zum Zwecke,
                    Wasser fließe
                    und mit reichem, vollem Schwalle
                    zu dem Bade sich ergieße.'''
temp_zwei_wochen = [27.7, 28.3, 28.0, 26.5, 25.3, 28.2, 25.9, 24.6, 24.0, 24.1, 23.4, 20.7, 21.2, 24.4]
temp_eine_woche = [25.4, 23.6, 23.4, 22.6, 24.9, 20.1, 19.5]

anzahl_chars = len(zauberlehrling)
print(f'Anzahl Charaktere: {anzahl_chars}')

zauberlehrling = zauberlehrling.replace('ß','ss')
print(zauberlehrling)

position = zauberlehrling.find('Zwecke')
print(f'Position des Wortes "Zwecke": {position}')




