constante = True
while constante:

    numero = str((input("Debe ingresar un numero: ")))

    while numero.isdigit() and int(numero) > 0:
        print (f'Su numero es {numero} es mayor a cero' )

        palabra = str(input("Ingrese una palabra o frase: "))
        cantidadPalabra = len(palabra)
        print (f'La palabra {palabra} tiene de largo {cantidadPalabra} ')

        resultado = 1
        for i in range (1 , cantidadPalabra + 1 , 1 ):
            resultado = resultado * (i)
        print(f'El resultado del factorial es: {resultado}')
        if (resultado % 2 == 0):
            print(f'El resultado: {resultado} es un numero par')
        else:
            print(f'El resultado:  {resultado} es un numero impar')
        break
    if ( numero.isalpha() or int(numero) <= 0 ):
        print ("No se ingreso un numero o fue menor o igual a 0")
        break