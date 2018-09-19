# # # # # # # # # # # # # # # # # # # # # # # # #
#
# ¡Ahora otro Kata!
#
# El objetivo será crear una función que nos devuelva
# el promedio de una lista de enteros.
#
# El promedio es la suma de todos los elementos,
# dividida entre el número total de elementos.
#
# Cabe destacar que el resultado podría ser un
# número decimal o "float".
#
# Mucho éxito!


def promedio(lista):
    #### ESCRIBIR CÓDIGO AQUÍ ####

    return sum(lista) / float(len(lista))

    ###############################



print(promedio([1, 8, 3, 4, 7, 9]))                          # Respuesta: 5.333333333
print(promedio([9, 9, 8, 8]))                                # Respuesta: 8.5
print(promedio([4, 3, 2, 1, 3]))                             # Respuesta: 2.6
print(promedio([16, 49, 111, 0, -5, 17, 9, 8, 16, 46,
                23, 67, 321, 3, 678, 342, 101, 66, 21]))     # Respuesta: 99.42105263
