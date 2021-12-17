'''                                             Ejercicio 1
Escribe una función llamada ejercicio1 que genere una lista con 15 valores enteros aleatorios que vayan de 1 a 100. 
La función debe devolver la lista con todos los valores.'''

import random
def ejercicio1 ():
    lista = []
    for valor in range(15):
        randomValue = random.randint(0, 100)
        lista.append(randomValue)
    return lista


print(ejercicio1())