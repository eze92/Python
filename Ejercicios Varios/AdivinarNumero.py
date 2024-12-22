import random

print("Ingrese un numero si el numero es correcto el juego termina de lo contrario termina el 5to intento")

numero_secreto = random.randint(1, 50)
contador = 0

##print(numero_secreto)

while contador < 5 :
    numero = int(input("Ingrese un numero que debe estar entre 1 y 50 :"))
    contador = contador + 1

    print("Numero de intentos", contador)
    if (numero_secreto == numero) :
        print (f'El numero secreto era {numero_secreto} a acertado!!')
    elif numero_secreto > numero:
        print("El numero secreto es mayor al ingresado")
    else:
        print("El numero secreto es menor al ingreado")
if (contador == 5) :
    print(f'Ya realizo los 5 intentos el numero secreto era {numero_secreto}')

