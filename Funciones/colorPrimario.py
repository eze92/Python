def colorPrimario( color):
    if (color.lower() == 'rojo' or color.lower() == 'azul'  or color.lower() == 'amarillo') :
        print (f'El {color} es un color primario')
    else:
        print (f'El {color} no es un color primario')
    return


color = 'rojo'
colorPrimario(color)

