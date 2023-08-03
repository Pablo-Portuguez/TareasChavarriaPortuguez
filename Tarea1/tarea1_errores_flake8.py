# Autores: Joel David Chavarría González y Pablo Portuguez Peraza
# Curso de Microcontroladores y Microprocesadores
# Tarea 1
#Errores identificables por flake8
"""
.\Tarea1\tarea1_errores_flake8.py:4:1: E265 block comment should start with '# '
.\Tarea1\tarea1_errores_flake8.py:7:12: E225 missing whitespace around operator
.\Tarea1\tarea1_errores_flake8.py:9:5: F841 local variable 'Numero3' is assigned to but never used
"""

def SumaSimple():
    Numero1=3
    Numero2 = 8
    Numero3 = 0

    Resultado = Numero1 + Numero2

    print(Resultado)


SumaSimple()
