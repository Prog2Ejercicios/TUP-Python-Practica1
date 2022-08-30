""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

import string


lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO
tupla=tuple (lista)
# COMPLETAR - FIN
print(tupla)
assert tupla == ("casa", "perro", "pato", "gato")


"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

# COMPLETAR - INICIO
lista=list(tupla)
# COMPLETAR - FIN
print(lista)
assert lista == ["casa", "perro", "pato", "gato", "tenedor"]


"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

# COMPLETAR - INICIO
(a,b,c)=tupla
# COMPLETAR - FIN

assert a == "primer" and b == 25 and c == [1, 2, 3]


"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO
(a,b,c,d,e,f)=tupla
total=a+b+c+d+e+f
# COMPLETAR - FIN

assert total == 300


"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO
(e,m,s,a,c)=lista

string_concatenado= f"{e} {m} {s} {a} {c}"
# COMPLETAR - FIN
print(string_concatenado)

assert string_concatenado == "esta mañana sali a correr"


"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO
(primer,b,c,d,e)=tupla
# COMPLETAR - FIN
print(primer)
assert primer == 73


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO
(a,b,c,d,e)=lista
suma=(a+e)
# COMPLETAR - FIN
print(suma)
assert suma == 75


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO
(a,b,c,d,e,f,g,h,i)=tupla
string_concatenado= f"{a} {b} {c} {d} {e}"
# COMPLETAR - FIN
print(string_concatenado)
assert string_concatenado == "anoche fui a la fiesta"