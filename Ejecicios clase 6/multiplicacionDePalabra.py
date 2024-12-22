palabra = str(input("Ingrese una palabra: "))
numero = int(input("ingrese un numero: "))

for contador in range(numero):
    print(f"{contador++1}- {palabra}")