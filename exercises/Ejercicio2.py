"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True
piso_mojado = bool
# COMPLETAR - INICIO
if esta_lloviendo == True or riego_activado == True:
    piso_mojado = True
    print(piso_mojado)
# COMPLETAR - FIN

assert piso_mojado == True


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)
area_mayor_a_cinco = bool
# COMPLETAR - INICIO
if not area_cuadrado <= 5:
    area_mayor_a_cinco = True
    print("El area del cuadrado es mayor a 5")
# COMPLETAR - FIN

assert area_mayor_a_cinco == True


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50
resultado = bool
# COMPLETAR - INICIO
if numero_1 % 7 == 0 and numero_2 % 7 != 0:
    resultado = True
    print(resultado)
# COMPLETAR - FIN

assert resultado == True


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

# COMPLETAR - INICIO
resultado = (variable_01 or variable_02) and variable_03 or (variable_04 and variable_05)
print(resultado)
# COMPLETAR - FIN

assert resultado == 80