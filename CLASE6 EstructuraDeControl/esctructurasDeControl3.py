condicion = True
nota2 = "ha"

while condicion:
    nota = input("Ingrese contraseña: ")

    if nota == nota2:
        condicion = False
        print("Bienvenido")