from tkinter import *

def soma():


    var1 = int(in1.get())
    var2 = int(in2.get())
    soma = var1 + var2
    lb1['text'] = soma




janela = Tk()
janela.geometry('400x300+500+500')
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)

lb1 = Label(janela, text='Resultado', font='Arial 26')
in1 = Entry(janela, font='Arial 26')
in2 = Entry(janela, font='Arial 26')
bt1 = Button(janela,text='Soma', font='Arial 26', command=soma)

lb1.pack()
in1.pack()
in2.pack()
bt1.pack()


janela.mainloop()