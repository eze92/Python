from tkinter import Tk,Entry

ventana = Tk()

ventana.configure(background='blue')
ventana.title('Calculadora Basica')
ventana.geometry('350x350')
ventana.resizable(False,False)

datos = Entry(ventana)


ventana.mainloop()