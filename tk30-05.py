from tkinter import *

#back-end
def imprimir():
    lb1['text'] = in1.get()
    print(in1.get())

#window
janela = Tk()
#geometria
janela.geometry('400x300+500+500')
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)

#widget
lb1 = Label(janela, text='Olá mundo!', font='Arial 26', fg='purple')
in1 = Entry(janela, font='Arial 26')
bt1 = Button(janela,text='Sair', font='Arial 26',command=quit)



#layout
lb1.pack()
in1.pack()
bt1.pack()


#run
janela.mainloop()