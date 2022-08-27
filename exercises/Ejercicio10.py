"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

from tkinter import Variable


A = 5

# COMPLETAR - INICIO
if A == 5:
    variable_01 = True
    print(variable_01)
# COMPLETAR - FIN

assert variable_01 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = "Lavaye"

# COMPLETAR - INICIO
if not Domicilio == "Lavalle":
    variable_02 = False
    print(variable_02)
# COMPLETAR - FIN

assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

# COMPLETAR - INICIO
if Domicilio == "Alsina 2446" or "Pueyrredón y la vía":
    variable_03 = True
    print(variable_03)
# COMPLETAR - FIN

assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

# COMPLETAR - INICIO
if lista_de_compras == "No comprar nada" or ["Pan", "Aceite", "Sal"]:
    variable_04 = True
    print(variable_04)
# COMPLETAR - FIN

assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

# COMPLETAR - INICIO
if lista_de_ids == 0 and [1236, 5565, 8956, 2534]:
    variable_05 = False
    print(variable_05)
# COMPLETAR - FIN

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

# COMPLETAR - INICIO
if diccionario == {} and {"Nombre": "Alberto Paz", "DNI": 12365855}:
    variable_06 = False
print(variable_06)
# COMPLETAR - FIN

assert variable_06 is False