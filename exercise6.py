"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""
lista_01 = []

lista_01.append(5)
lista_01.append(0)
lista_01.append(8)
lista_01.append(8)

print(len(lista_01))

assert len(lista_01) == 4



"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

elemento_extraido = lista.pop(3)

print(elemento_extraido)

assert elemento_extraido == 6


"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]
listas_concatenadas_01 = []


lista_a = str(lista_a)


listas_concatenados_01 = lista_a.extend(lista_c)

print(listas_concatenadas_01)

assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]



"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

lista_nueva.insert(2, variable_01)

print(lista_nueva)

assert lista_nueva == [0, 1, 2, 3, 4]


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]
lista_primero_y_ultimo = []
primero = lista.pop(0)
ultimo = lista.pop(-1)

lista_primero_y_ultimo = primero + ultimo

print(lista_primero_y_ultimo)

assert lista_primero_y_ultimo == ["ho", "la"]



"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

lista_primeros  = lista[:3]

print(lista_primeros)

assert lista_primeros == ["ho", 3.1416, "la"]



"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]
lista_primeros_y_ultimos = [4]

lista_primeros_y_ultimos[0] = lista.pop(0)
lista_primeros_y_ultimos[1] = lista.pop(-1)



print(lista_primeros_y_ultimos)

assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]


"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

lista_concatenada = lista_01 + lista_02

print(lista_concatenada)

assert lista_concatenada == [0, 1, 2, 3, 5, 6]




"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

lista_duplicada = lista_01 * 3

print(lista_duplicada)

assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]



"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

variable_booleana = elemento in lista

print(variable_booleana)

assert variable_booleana



"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

son_iguales = lista_01 == lista_02

print(son_iguales)

assert not son_iguales



"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

desaprobado = False
no_tiene_examenes_aprobados = any(notas)

print(no_tiene_examenes_aprobados == desaprobado)

assert no_tiene_examenes_aprobados


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

tiene_todo_aprobado = all(notas)

print(tiene_todo_aprobado)

assert not tiene_todo_aprobado

