from tkinter import *

root=Tk()
root.title('Cadastro')
root.geometry('459x620')
root.minsize(width=100, height=100)
root.maxsize(width=459, height=620)


fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)


#fr1
lb1_fr1 = Label(fr1, text='Dados Pessoais', font='Times 20',fg='red')
in1 = Entry(fr1)
lb2_fr1 = Label(fr1, text='Nome:', font='times 17')
lb3_fr1 = Label(fr1, text='Data Nasc:', font='Times 17')
in2 = Entry(fr1)
lb4_fr1 = Label(fr1, text='CPF:', font='Times 17')
in3 = Entry(fr1)
lb5_fr1 = Label(fr1, text='Telefone:', font='Times 17')
in4 = Entry(fr1)


#fr2
lb6_fr2 = Label(fr2, text='Endereço', font='Times 20',fg='red')
lb7_fr2 = Label(fr2, text='Rua:', font='Times 17')
in5 = Entry(fr2)
lb8_fr2 = Label(fr2, text='Nº:', font='Times 17')
in6 = Entry(fr2)
lb9_fr2 = Label(fr2, text='Bairro:', font='Times 17')
in7 = Entry(fr2)
lb10_fr2 = Label(fr2, text='Cidade:', font='Times 17')
in8 = Entry(fr2)

#fr3
bt1_fr3 = Button(fr3, text='Gravar Dados',fg='black',activebackground='grey',bg='grey',activeforeground='red', font='Arial 23')
bt2_fr3 = Button(fr3, text='Listar Dados', fg='black',activebackground='grey',bg='grey',activeforeground='red', font='Arial 23')



lb1_fr1.grid(row=0,column=0,padx= 1, pady=10)
in1.grid(row=3,column=2,padx= 1, pady=10)
lb2_fr1.grid(row=3,column=0,padx= 1, pady=10)
lb3_fr1.grid(row=4,column=0,padx= 1, pady=10)
in2.grid(row=4,column=2,padx= 1, pady=10)
lb4_fr1.grid(row=5,column=0,padx= 1, pady=10)
in3.grid(row=5,column=2,padx= 1, pady=10)
lb5_fr1.grid(row=6,column=0,padx= 1, pady=10)
in4.grid(row=6,column=2,padx= 1, pady=10)

lb6_fr2.grid(row=0,column=0,padx= 1, pady=10)
lb7_fr2.grid(row=7,column=0,padx= 1, pady=10)
in5.grid(row=7,column=2,padx= 1, pady=10)
lb8_fr2.grid(row=8,column=0,padx= 1, pady=10)
in6.grid(row=8,column=2,padx= 1, pady=10)
lb9_fr2.grid(row=9,column=0,padx= 1, pady=10)
in7.grid(row=9,column=2,padx= 1, pady=10)
lb10_fr2.grid(row=10,column=0,padx= 1, pady=10)
in8.grid(row=10,column=2,padx= 1, pady=10)

bt1_fr3.grid(row=8,column=10,padx=2, pady=10)
bt2_fr3.grid(row=8,column=15,padx=2, pady=10)



fr1.pack()
fr2.pack()
fr3.pack()



root.mainloop()
