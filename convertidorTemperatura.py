from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk

def convertir():
    if not valor_entrada.get().isdigit():
        messagebox.showerror("Error", "Por favor, ingrese un número válido para la temperatura.")
        return
    
    valor = float(valor_entrada.get())
    desde = combo_desde.current()
    a = combo_a.current()
    
    #desde == 0  y a == 1  significa el combo que estan eligiendo, desde == 0 primer combo, a ==1 segundo combo
    if desde == 0 and a == 1:
        resultado = (valor * 9/5) + 32
    elif desde == 1 and a == 0:
        resultado = (valor - 32) * 5/9
    else:
        resultado = valor  # Si se seleccionan las mismas unidades, no se hace conversión

    resultado_label.config(text=f"Resultado: {resultado:.2f}")

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Configuración de la ventana
ventana= Tk()
ventana.configure(background='#3346FF')
ventana.title("Convertidor Temperatura Celsius/Fahrenheit")
ventana.resizable(0,0)


# Ajustar el tamaño de la ventana
ventana.geometry("500x250")

# Campo de entrada
label_valor = Label(ventana, width=70,background='#3346FF', font=("Arial", 12, "bold"), foreground="white",text="Temperatura:")
label_valor.pack()
valor_entrada = ttk.Entry(ventana)
valor_entrada.pack()

# Combobox para seleccionar Celsius o Fahrenheit en el primer combo
label_desde = Label(ventana,width=70,background='#3346FF', font=("Arial", 12, "bold"), foreground="white", text="Desde:")
label_desde.pack()
combo_desde = ttk.Combobox(ventana, values=["Celsius", "Fahrenheit"])
combo_desde.pack()

# Combobox para seleccionar Celsius o Fahrenheit en el segundo combo
label_a = Label(ventana,width=70,background='#3346FF',font=("Arial", 12, "bold"),  foreground="white",text="A:")
label_a.pack()
combo_a = ttk.Combobox(ventana, values=["Celsius", "Fahrenheit"])
combo_a.pack()

# Botón de conversión
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack()

# Etiqueta para mostrar el resultado
resultado_label = Label(ventana,width=70,background='#3346FF',font=("Arial", 12, "bold"), text="")
resultado_label.pack()

# Botón para cerrar la ventana
boton_cerrar = ttk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()


# Iniciar el bucle de eventos
ventana.mainloop()
