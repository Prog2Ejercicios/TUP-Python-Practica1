variable_01 = "Le debo "
variable_02 = 6
variable_03 = " pesos a un amigo hace "
variable_04 = " años."
variable_05 = "Ezequiel"

# COMPLETAR - INICIO
strings_concatenados = variable_01 + "{}".format(variable_02) + variable_03 + "{}".format(variable_02) + variable_04 + " Se llama {}".format(variable_05)
# COMPLETAR - FIN

assert (
    strings_concatenados == "Le debo 6 pesos a un amigo hace 6 años. Se llama Ezequiel"
)
