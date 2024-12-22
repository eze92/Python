from tkinter import Tk, Entry, Button, StringVar

digito = ''

def tomar_digito(n):
    global digito
    digito = digito + str(n)
    #print(digito)
    calculo.set(digito)

def resultado():
    try:
        global digito
        #print(digito)
        total = str(eval(digito))
        calculo.set(total)
        digito = ''
    except:
        calculo.set("ERROR")

def limpiar_todo():
    global digito
    calculo.set("")
    digito = ""

ventana = Tk()

ventana.configure(background='#FF5733')
ventana.title('Calculadora Basica')
ventana.geometry('350x350') #Ancho x Alto
ventana.resizable(0,0)

calculo = StringVar()

datos = Entry(ventana, width=60, textvariable=calculo)
datos.grid(row=0 , column=0, columnspan=10)

btn1 = Button(ventana, text='1' , bg='blue' , fg='white',width=11 , height=2, command= lambda: tomar_digito(1))
btn1.grid(row=1 , column=0)

btn2 = Button(ventana, text='2' , bg='blue' , fg='white',width=11 , height=2, command= lambda: tomar_digito(2))
btn2.grid(row=1 , column=1)

btn3 = Button(ventana, text='3' , bg='blue' , fg='white',width=11 , height=2, command= lambda: tomar_digito(3))
btn3.grid(row=1 , column=2)

btnMas = Button(ventana, text='+' , bg='blue' , fg='white',width=11 , height=2 ,command= lambda: tomar_digito('+'))
btnMas.grid(row=1 , column=3)

btn4 = Button(ventana, text='4' , bg='blue' , fg='white',width=11 , height=2)
btn4.grid(row=2 , column=0)

btn5 = Button(ventana, text='5' , bg='blue' , fg='white',width=11 , height=2)
btn5.grid(row=2 , column=1)

btn6 = Button(ventana, text='6' , bg='blue' , fg='white',width=11 , height=2)
btn6.grid(row=2 , column=2)

btnResta = Button(ventana, text='-' , bg='blue' , fg='white',width=11 , height=2)
btnResta.grid(row=2 , column=3)

btn7 = Button(ventana, text='7' , bg='blue' , fg='white',width=11 , height=2)
btn7.grid(row=3 , column=0)

btn8 = Button(ventana, text='8' , bg='blue' , fg='white',width=11 , height=2)
btn8.grid(row=3 , column=1)

btn8 = Button(ventana, text='9' , bg='blue' , fg='white',width=11 , height=2)
btn8.grid(row=3 , column=2)

btnPor = Button(ventana, text='*' , bg='blue' , fg='white',width=11 , height=2)
btnPor.grid(row=3 , column=3)

btn0 = Button(ventana, text='0' , bg='blue' , fg='white',width=11 , height=2)
btn0.grid(row=4 , column=0)

btnDec = Button(ventana, text='.' , bg='blue' , fg='white',width=11 , height=2)
btnDec.grid(row=4 , column=1)

btnC = Button(ventana, text='C' , bg='blue' , fg='white',width=11 , height=2, command=limpiar_todo)
btnC.grid(row=4 , column=2)

btnDividir = Button(ventana, text='/' , bg='blue' , fg='white',width=11 , height=2)
btnDividir.grid(row=4 , column=3)

btnPA = Button(ventana, text='(' , bg='blue' , fg='white',width=11 , height=2)
btnPA.grid(row=5 , column=0)

btnIgual = Button(ventana, text='=' , bg='blue' , fg='white',width=24 , height=2, command=resultado)
btnIgual.grid(row=5 , column=1 , columnspan=2)

btnPC = Button(ventana, text=')' , bg='blue' , fg='white',width=11 , height=2)
btnPC.grid(row=5 , column=3)

ventana.mainloop()