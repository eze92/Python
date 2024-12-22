def restar(x,y):
    #print("Hola estoy aca")
    return x-y
    

def restar2(x,y):
    r = x-y
    print(f"Tu resta es: {r}")


restar2(restar(3,4),restar(1,2))

resta = restar(5,1)

print(resta)


def sumar5(x):
    print(f"Al numero {x} se le sumo 5 y da: {5+x}")

sumar5(10)


def pedir_nombre():
    return input("Ingrese su nombre: ")

#print(f"Su nombre es: {pedir_nombre()}")

def resta3():
    r = restar(9,1) - restar(1)

    return r

#print(resta3())

def sumar2(x,z=0,y=3):
    
    return x+y+z

print(sumar2(2))

nombre = "gabriel"

def cambiar_nombre(n):
    nombre = n + "hola"
    print(nombre)

cambiar_nombre(nombre)
print(nombre)
    