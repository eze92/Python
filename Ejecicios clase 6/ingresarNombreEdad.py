try:
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese la edad: "))

    if ( numero >= 18):
        print(f'{nombre} tiene {numero} años, por lo tanto es mayor de edad')
    else:
        print(f'{nombre} tiene {numero} años, por lo tanto es menor de edad')
except:
    print("Debe ingresar edad correcta ")
    