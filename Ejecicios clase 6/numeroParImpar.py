
try:
    numero = int(input("Ingrese un numero a evaluar: "))

    if ( numero % 2 == 0 ) :
        print("El numero ingresado es par")
    else:
        print ("El numero ingresado es impar")
except:
    print("Debe ingresar un numero entero")