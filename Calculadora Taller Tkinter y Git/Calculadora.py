import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import Menu


def bienvenida():
    window = tk.Tk()
    window.title('Bienvenido')
    window.geometry('450x400')
    window.config(bg='Yellow')
    window.iconbitmap(r'd:\Personal\Downloads\Calculator_30001.ico')

    label= tk.Label(window, text = """Bienvenido Usuario,
    antes de acceder a la calculadora 
    puedes escoger el tema de esta,
    tienes por un lado
    el tema claro (Fondo blanco,letras oscuras)
    o el tema oscuro( Fondo negro,letras claras). """, font =('Arial bond', 15))
    label.grid(column = 0, row = 0)
    label.config(bg= 'yellow')

    rad1 = Radiobutton(window, text = 'Modo Oscuro', command= dark_mode)
    rad1.grid(column =0, row = 2 )
    

    rad2 = Radiobutton(window, text = 'Modo Claro', command= init_window)
    rad2.grid(column =0, row = 3 )

    window.mainloop()


def init_window():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x250')
    window.iconbitmap(r'd:\Personal\Downloads\Calculator_30001.ico')

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label ='Nueva Ventana', command = init_window)
    menu.add_cascade(label='Archivo', menu= new_item)
    window.config(menu=menu)

    label = tk.Label(window, text ='Calculadora', font=('Arial bond', 15))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)

    entrada1.grid (column = 1, row = 1)
    entrada2.grid (column = 1, row = 2)

    label_entrada1 = tk.Label (window, text = 'Ingrese primer numero: ', font = ('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label (window, text = 'Ingrese segundo numero: ', font = ('Arial bold', 10))
    label_entrada2.grid(column = 0, row = 2)

    label_operador = tk.Label(window, text = 'Escoja un operador', font =('Arial bond', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow', '√']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='Resultado: ', font = ('Arial bold', 15))
    label_resultado.grid(column=0 , row=5)

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                        label_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get()),
                    text='Calcular',
                    bg="purple",
                    fg="white")
    boton.grid(column = 1, row = 4)

    
    messagebox.showinfo('Uso de la Raiz',
         """Si quiere usar la función de raíz, tener en cuenta que el primer número sera el indice radical y el segundo el radicando""")


    

    window.mainloop()

def calculadora(num1,num2,operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 / num2, 2)
    elif operador == 'pow':
        resultado = num1 ** num2
    else:
        resultado = num2 ** (1/num1)
        
    
    return resultado

def click_calcular(label,num1,num2,operador):
    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    label.configure(text = 'Resultado: ' + str(res))


def dark_mode():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x250')
    window.config(background = 'Black')
    window.iconbitmap(r'd:\Personal\Downloads\Calculator_30001.ico')

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label ='Nueva Ventana', command = dark_mode)
    menu.add_cascade(label='Archivo', menu= new_item)
    window.config(menu=menu)

    label = tk.Label(window, text ='Calculadora',fg= 'white', font=('Arial bond', 15))
    label.grid(column = 0, row = 0)
    label.config(bg = 'black')

    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)

    entrada1.grid (column = 1, row = 1)
    entrada2.grid (column = 1, row = 2)

    label_entrada1 = tk.Label (window, text = 'Ingrese primer numero: ', fg= 'white', font = ('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)
    label_entrada1.config(bg = 'black')

    label_entrada2 = tk.Label (window, text = 'Ingrese segundo numero: ',fg='white', font = ('Arial bold', 10))
    label_entrada2.grid(column = 0, row = 2)
    label_entrada2.config(bg = 'black')

    label_operador = tk.Label(window, text = 'Escoja un operador',fg= 'white', font =('Arial bond', 10))
    label_operador.grid(column = 0, row = 3)
    label_operador.config(bg='black')

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow', '√']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='Resultado: ',fg='white', font = ('Arial bold', 15))
    label_resultado.grid(column=0 , row=5)
    label_resultado.config(bg='black')

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                        label_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get()),
                    text='Calcular',
                    bg="purple",
                    fg="white")
    boton.grid(column = 1, row = 4)

    
    messagebox.showinfo('Uso de la Raiz',
         """Si quiere usar la función de raíz, tener en cuenta que el primer número sera el indice radical y el segundo el radicando""")
    

    window.mainloop()


def main():
    bienvenida()

main()