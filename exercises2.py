"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

piso_mojado = esta_lloviendo and riego_activado

print(piso_mojado)

assert piso_mojado

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

from re import A


lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

area_mayor_a_cinco = lado_cuadrado and area_cuadrado > 5

print(area_mayor_a_cinco)

assert area_mayor_a_cinco



"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50
resultado = 0

if(numero_1 // 1) or (numero_2 // 1):
    resultado = True

print(resultado)

assert resultado

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""


variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100 



resultado = not(variable_01 > variable_02) or (variable_03 < variable_05)

if(resultado==True):
    resultado = variable_03
    print(resultado)
else:
    print("Respuesta incorrecta")

assert resultado == 80

 

