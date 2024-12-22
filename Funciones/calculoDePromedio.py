def calculoPromedio(numero):
    suma_numero = 0
    for i in numero:
       ## print( {i})
        suma_numero = suma_numero + i
    promedio = suma_numero / len(numero)
    return promedio
print(" El promedio es", calculoPromedio([2,1]))