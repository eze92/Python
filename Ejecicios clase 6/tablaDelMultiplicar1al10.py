
try:
    numero = int(input("Ingrese un numero: "))

    for i in range (1,11):
        resultado =  i * numero
        print(f'{numero} x {i} = {resultado}') 
except:
    print("Debe ingresar un numero entero ")
    