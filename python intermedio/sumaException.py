numero = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese un divisor: '))

try : 
    resultado = numero / numero2
    print (f"El resultado es {resultado}")
except  ZeroDivisionError:
    print ("No se puede dividir por 0")

