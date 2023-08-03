# Autores: Joel David Chavarría González y Pablo Portuguez Peraza
# Curso de Microcontroladores y Microprocesadores
# Tarea 1
# Verificación de funcionamiento de código mediante Pytest

# Método separa_letras
def separa_letras(cadena):
    # Declaración de todas las variables necesarias para la función
    cadenaMayus = ""
    cadenaMinus = ""
    res1 = ""
    res2 = ""
    estado = 0
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    # Caso string vacio
    if cadena == "":
        estado = -300
        res1 = None
        res2 = None
    # Caso string númerico
    elif isinstance(cadena, int) is True:
        estado = -100
        res1 = None
        res2 = None
    # Demas casos
    else:
        # Se recorre la cadena para encontrar mayúsculas y minúsculas
        for caracter in cadena:
            # Se localizan y concatenan las mayúsculas
            if caracter in mayusculas:
                cadenaMayus = caracter+cadenaMayus
                res1 = cadenaMayus[::-1]
                estado = 0
            # Se localizan y concatenan las minúsculas
            elif caracter in minusculas:
                cadenaMinus = caracter+cadenaMinus
                res2 = cadenaMinus[::-1]
                estado = 0
            # Caso en el que no es número ni letra (simbolos)
            else:
                estado = -200
                res1 = None
                res2 = None
    # variables resultantes para el pytest
    return estado, res1, res2


def potencia_manual(param1, param2):
    result = 0
    estado = 0

    # Caso en que entradas son variable de tipo numéricas
    if isinstance(param1, int) and isinstance(param2, int):
        estado = 0
        result = param1
        multi = param1
        if (param2 == 0):  # Caso particular, exponente es 0
            result = 1
            return estado, result

        else:
            """ Se repite la multiplicación por
            la cantidad de veces del exponente"""
            for i in range(param2-1):

                """ Se repite la suma por la cantidad de veces
                de la base (multiplicación)"""
                for x in range(param1-1):

                    # Se suma el número más el mismo
                    result = result + multi

                # Se actualiza el número que se está sumando
                multi = result

            return estado, result
    else:
        estado = -400
        result = None
        return estado, result
