"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

variable_01 = 5

variable_01 = variable_01 == A 

print(variable_01)

assert variable_01 is True



"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

variable = 3

variable_02 = variable == Domicilio

print(variable_02)

assert variable_02 is False




"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

variable = "Alsina 2446"

variable_03 = any(Domicilio)

print(variable_03)

assert variable_03 is True



"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

variable_04 = any(lista_de_compras)

print(variable_04)

assert variable_04 is True

"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

variable_05 = 0

variable_05 =  any.lista_de_ids

print(variable_05)

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

variable_06 = any(diccionario)

print(variable_06)

assert variable_06 is False