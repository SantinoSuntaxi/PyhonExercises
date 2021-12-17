'''Ejercicio 3
Usando funciones anónimas, crea una nueva lista que contenga 
los valores enteros de cada uno de los elementos de la lista que 
devuelve la función implementada en el Ejercicio 2.'''
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


def ejercicio3(newList):
    filtrado = filter(lambda x: x % 2 != 0, newList)
    dataFilter = []
    dataFilter = list(filtrado)
    return dataFilter

print(ejercicio3([2,3,5,10,15,20]))

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

dataFilter = []
dataFilter = list(filtrado)

print (dataFilter)