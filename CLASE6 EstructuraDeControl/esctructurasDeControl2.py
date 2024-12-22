total = 0

while cont <= 3:
    nota = input("Ingrese nota: ")
    suma = f"{suma} + {nota}"
    total = eval(suma)
    suma = total
    print(cont)
    cont += 1 #cont = cont +1

print(f"La suma es: {suma} y contador quedo en: {cont}")

