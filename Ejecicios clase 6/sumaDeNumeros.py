print("Se sumaran todos los numeros ingresados hasta que ingrese uno distinto de 0")
suma = 0
numero = 1
while numero != 0 :
    try:
        numero = int(input("Ingrese un numero: "))
        suma = suma + numero 
    except:
        print("Debe ingresar un numero entero")
print (f'El resutaltado de la suma es : {suma}')
   

