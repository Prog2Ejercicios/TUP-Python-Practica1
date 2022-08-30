"""Coerción a Booleanos"""


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_01
"""

A = 5

# COMPLETAR - INICIO
if A % 2 == 0:
    A = False
elif A % 2 == 1:
    A = True 
variable_01 = A

# COMPLETAR - FIN

assert variable_01 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_02
"""

Domicilio = ""

# COMPLETAR - INICIO
Domicilio = 0 
Domicilio = False
variable_02 = Domicilio
# COMPLETAR - FIN

assert variable_02 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

# COMPLETAR - INICIO
Domicilio = 1 * 1
Domicilio = True
variable_03 = Domicilio
# COMPLETAR - FIN

assert variable_03 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

# COMPLETAR - INICIO
lista_de_compras = 0 + 1
lista_de_compras= True
variable_04 = lista_de_compras
# COMPLETAR - FIN

assert variable_04 is True


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_05
"""

lista_de_ids = 0 and [1236, 5565, 8956, 2534]

# COMPLETAR - INICIO
lista_de_ids = 0 + 1
lista_de_ids =True
variable_05 = not lista_de_ids
 
# COMPLETAR - FIN

assert variable_05 is False


"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

# COMPLETAR - INICIO
diccionario= 0 + 1
diccionario = True
variable_06 = not diccionario
# COMPLETAR - FIN

assert variable_06 is False