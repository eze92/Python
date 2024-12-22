def acceder_clave(diccionario, clave):

  try:
    valor = diccionario[clave]
    print(f"El valor asociado a la clave '{clave}' es: {valor}")
  except KeyError:
    print(f"La clave '{clave}' no existe en el diccionario.")


mi_diccionario = {'nombre': 'Juan', 'edad': 30}


acceder_clave(mi_diccionario, 'nombre')


acceder_clave(mi_diccionario, 'ciudad')