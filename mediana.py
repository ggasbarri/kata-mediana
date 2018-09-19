# # # # # # # # # # # # # # # # # # # # # # # # #
#
# Buen día a todos!
#
# El objetivo de este Kata es crear una funcion que
# dada una lista de n elementos enteros, devuelva la
# mediana de dicha lista.
#
# La mediana es el número central de una lista, una
# vez que la misma ha sido ordenada. En otras palabras,
# si una lista tiene 5 elementos, la mediana será el
# tercer elemento una vez que esté ordenada.
#
# Cabe destacar que si la lista tiene un número par de
# elementos, por ejemplo 6 elementos; la mediana serán
# los dos números centrales una vez que esté ordenada,
# siendo para este ejemplo los elementos 3 y 4.
#
# Para facilitar de la resolución, les comentamos que
# una lista se puede ordenar de dos formas:
#
# 1- lista_ordenada = sorted(lista)
#
# 2- lista.sort()
#
# Mucho éxito!

import math


def mediana(lista):
    #### ESCRIBIR CODIGO AQUI ####

    lista_ordenada = sorted(lista)
    longitud = len(lista)
    med = []

    if (longitud % 2) == 0:
        mitad = int(len(lista) / 2.0)
        med.append(lista_ordenada[mitad - 1])
        med.append(lista_ordenada[mitad])
    else:
        med.append(lista_ordenada[math.floor(len(lista) / 2.0)])

    return med

    ###############################


print(mediana([1, 8, 3, 4, 7, 9]))                          # Respuesta: [4, 7]
print(mediana([9, 9, 8, 8]))                                # Respuesta: [8, 9]
print(mediana([4, 3, 2, 1, 3]))                             # Respuesta: [3]
print(mediana([16, 49, 111, 0, -5, 17, 9, 8, 16, 46,
               23, 67, 321, 3, 678, 342, 101, 66, 21]))     # Respuesta: [23]
