#Ingrese 5 numeros y calcular el promedio

print("Ingrese 5 numeros para calcular el promedio de su suma")

try:
    numero =  float(input('Ingrese el primer numero: '))

    numero2 = float(input('Ingrese el segundo numero: '))

    numero3 = float(input('Ingrese el tercer numero: '))

    numero4 = float(input('Ingrese el cuarto numero: '))

    numero5 = float(input('Ingrese el quinto numero: '))

    calculo = float(numero+ numero2 + numero3 + numero4 + numero5 ) / 5

    print("El promedio es:" , calculo)

except:print("No se ingreso un numero")
