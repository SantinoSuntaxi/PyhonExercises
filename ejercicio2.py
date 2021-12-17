'''Ejercicio 2
Escribe una función llamada ejercicio2 que recibe 2 argumentos: el primero será la lista que hemos implementado en el Ejercicio 1 
y el segundo un número por el que se dividirá cada uno de los elementos de la lista.
 El resultado será una nueva lista.'''

import random
def ejercicio1 ():
    lista = []
    for valor in range(15):
        randomValue = random.randint(0, 100)
        lista.append(randomValue)
    return lista

def ejercicio2 (lista,divisor):
    newList = []
    for valores in lista:
        newList.append(valores/divisor)
    return newList

ejercicio1
#print (ejercicio2([4,8,10],4))
#print (ejercicio1())
print (ejercicio2(ejercicio1(),4))
