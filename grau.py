from tkinter import *

root = Tk()
root.title('Conversor')
fr1 = Frame(root,bg='grey')
fr2 = Frame(root,bg='white')

def converter():
   c = float(in1.get())
   f = c * 1.8 + 32
   lb2['text'] = f


lb1 = Label(fr1, text='C°', font='Times 30')
lb2 = Label(fr2, text='Resultado', font='Arial 25')
bt1 = Button(fr2, text='Converter',activebackground='orange', font='Arial 25', command=converter)
in1 = Entry(fr1, font="Arial 16")

fr1.pack()
fr2.pack()



lb1.grid(row=2,column=0, padx= 10, pady=10)
in1.grid(row=6,column=7, padx= 10, pady=10)
lb2.grid(row=6,column=8, padx= 10, pady=10)
bt1.grid(row=10,column=7, padx= 10, pady=10)


root.mainloop()