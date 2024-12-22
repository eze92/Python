
numero = int(input('Ingrese un numero: '))
valor = str(input('Ingrese un string: '))

try:
    resultado = numero + valor
except TypeError:
    print("No se puede sumar un numero y una cadena de caracteres")

