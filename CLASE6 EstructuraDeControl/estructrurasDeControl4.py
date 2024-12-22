acumulador = 0

#generalmente usamo i , ya que se indica que es un indice
for i in range(5):
    calificacion = input(f"Ingrese nota {i+1}: ") #recuerden que i arranca desde 0, por eso mostramos el +1
    acumulador +=  int(calificacion)


print(f"El promedio es: {acumulador/(i+1)}")


acumulador = 0 #reseteamos acumulador

for i in range(1,6):
    calificacion = input(f"Ingrese nota {i}: ") 
    acumulador +=  int(calificacion)


print(f"El promedio es: {acumulador/(i)}")


acumulador = 0 #reseteamos acumulador

for i in range(1,6,1):
    calificacion = input(f"Ingrese nota {i}: ") 
    acumulador +=  int(calificacion)


print(f"El promedio es: {acumulador/(i)}")