"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO

string_to_int_num1 =int(numero_01)
string_to_int_num2 =int(numero_02)
string_to_int_num3 =int(numero_03)
string_to_int_num4 =int(numero_04)

suma_de_numeros = string_to_int_num1  + string_to_int_num2  + string_to_int_num3   + string_to_int_num4

# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO

int_to_str_num01 = str(numero_01)
int_to_str_num02 = str(numero_02)
int_to_str_num03 = str(numero_03)

suma_de_numeros_string = int_to_str_num01 + int_to_str_num02 + int_to_str_num03

# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO

bin_to_int = int ("0b111010110101110111101000000", 2)
oct_to_int = int ("0o1425", 8)
hex_to_int = int ("0x6f540", 16)

multiplicacion_de_numeros = bin_to_int * oct_to_int * hex_to_int

# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO

str_to_int_num1 = int("987")
hex_to_int_num2 = int ("0x6f54F", 16)
oct_to_int_num3 = int ("0o1234", 8)

resultado_resta =  str_to_int_num1 - hex_to_int_num2 - oct_to_int_num3 - numero_04

# COMPLETAR - FIN

assert resultado_resta == -456350