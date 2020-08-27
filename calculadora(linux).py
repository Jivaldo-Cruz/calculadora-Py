#calculadora com python + tkinter
from tkinter import *

#------------------------------------------
# configuração inicial
root = Tk()
root.title("Calculadora simples")
root.resizable(False, False)

#------------------------------------------
# código lógico
show = ""
total = StringVar()
total.set("0")
lista = list()

def receber(num):
    global show
    lista.append(num)
    show = show + str(num)
    total.set(show)

def calc():
    x = str(lista)
    for char in "',[] ":
        x =  x.replace(char, "")
    total.set(eval(x))

def clear_total():
    global show
    global lista
    lista = []
    show = "0"
    total.set(show)


def clear():
    global show
    show = str()
    try:
        lista.pop()
        for x in lista:
            show += str(x)
        total.set(show)
    except IndexError:
        total.set("Error")

def exit_dvez():
    return exit()


#------------------------------------------
# menu
menu_ = Menu(root)

menu_.add_command(label = "Clear", command = lambda: clear_total())
menu_.add_command(label = "Fechar", command = lambda: exit_dvez())

root.config(menu = menu_)


#------------------------------------------
# configuração de widgets
campo = Label(root, width = 30, height = 2, background = "#ccc", textvariable = total, anchor = "e", border = 1, relief = "solid", highlightbackground = "#414146", highlightthickness = 3)

btn_9 = Button(root, text = "9", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(9))
btn_8 = Button(root, text = "8", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(8))
btn_7 = Button(root, text = "7", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(7))
btn_6 = Button(root, text = "6", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(6))
btn_5 = Button(root, text = "5", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(5))
btn_4 = Button(root, text = "4", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(4))
btn_3 = Button(root, text = "3", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(3))
btn_2 = Button(root, text = "2", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(2))
btn_1 = Button(root, text = "1", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(1))
btn_0 = Button(root, text = "0", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(0))
btn_mais = Button(root, text = "+", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("+"))
btn_menos = Button(root, text = "-", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("-"))
btn_mult = Button(root, text = "x", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("*"))
btn_div = Button(root, text = "/", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("/"))
btn_resto = Button(root, text = "%", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("%"))
btn_pe = Button(root, text = "(", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("("))
btn_pd = Button(root, text = ")", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber(")"))
btn_ponto = Button(root, text = ".", fg = "#fff", background = "#414146", width = 4, height = 2, command = lambda: receber("."))
btn_clear = Button(root, text = "Apagar", fg = "#fff", background = "red", width = 4, height = 2, command = lambda: clear())
btn_total = Button(root, text = "=", fg = "#fff", background = "red", width = 4, height = 2, command = lambda: calc())

campo.grid(row = 0, column = 0, columnspan = 4)
btn_9.grid(row = 1, column = 0, sticky = "w")
btn_8.grid(row = 1, column = 1, sticky = "w")
btn_7.grid(row = 1, column = 2, sticky = "w")
btn_6.grid(row = 2, column = 0, sticky = "w")
btn_5.grid(row = 2, column = 1, sticky = "w")
btn_4.grid(row = 2, column = 2, sticky = "w")
btn_3.grid(row = 3, column = 0, sticky = "w")
btn_2.grid(row = 3, column = 1, sticky = "w")
btn_1.grid(row = 3, column = 2, sticky = "w")
btn_0.grid(row = 4, column = 0, sticky = "w")
btn_mais.grid(row = 1, column = 3, sticky = "w")
btn_menos.grid(row = 2, column = 3, sticky = "w")
btn_mult.grid(row = 3, column = 3, sticky = "w")
btn_div.grid(row = 4, column = 2, sticky = "w")
btn_resto.grid(row = 4, column = 1, sticky = "w")
btn_total.grid(row = 4, column = 3, sticky = "w")
btn_ponto.grid(row = 5, column = 0, sticky = "w")
btn_pe.grid(row = 5, column = 1, sticky = "w")
btn_pd.grid(row = 5, column = 2, sticky = "w")
btn_clear.grid(row = 5, column = 3, sticky = "w")

#------------------------------------------
# configuração de loop
root.mainloop()
