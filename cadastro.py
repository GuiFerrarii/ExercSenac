from tkinter import *

root= Tk()
root.title('Cadastro')
root.geometry('459x620')
root.minsize(width=100, height=100)
root.maxsize(width=459, height=620)

#verifica data
def data(event=None):
    x=in2_fr1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in2_fr1.delete(0, 'end')
    in2_fr1.insert(0, y)




#Verifica_cpf
def capitura(event=None):
    x=in3_fr1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in3_fr1.delete(0, 'end')
    in3_fr1.insert(0, y)





fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
#caps primeira letra
var=StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)



#fr1
lb1_fr1 = Label(fr1, text='Dados Pessoais', font='Times 20',fg='red')
in1_fr1 = Entry(fr1, font='times 13', textvariable=var)
lb2_fr1 = Label(fr1, text='Nome:', font='times 17')
lb3_fr1 = Label(fr1, text='Data Nasc:', font='Times 17')
in2_fr1 = Entry(fr1, font='times 13')
in2_fr1.insert(0, 'DD/MM/AA')
in2_fr1.bind("<KeyRelease>", data)
lb4_fr1 = Label(fr1, text='CPF:', font='Times 17')
in3_fr1 = Entry(fr1, font='times 13')
in3_fr1.bind("<KeyRelease>", capitura)
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
bt3_fr1 = Button(fr1, text='Salvar',fg='black',activebackground='grey',bg='grey',activeforeground='red', font='Arial 23', command=lambda: [fr3.grid_forget(), fr2.grid(row=0, column=2), fr1.grid(row=6,column=2)])
bt4_fr1 = Button(fr1, text="Voltar ",fg='black',activebackground='grey',bg='grey', font="Arial 23",activeforeground='red', command=lambda: [fr1.grid_forget(), fr2.grid_forget(), fr3.grid(row=1, column=0, sticky=NSEW)])

#fr3
bt1_fr3 = Button(fr3, text='Cadastrar',fg='black',activebackground='grey',bg='grey',activeforeground='red', font='Arial 23', command=lambda: [fr3.grid_forget(), fr2.grid(row=0, column=2), fr1.grid(row=6,column=2)])
bt2_fr3 = Button(fr3, text='Entrar', fg='black',activebackground='grey',bg='grey',activeforeground='red', font='Arial 23')





lb1_fr1.grid(row=0,column=0)
in1_fr1.grid(row=3,column=2,padx= 1, pady=10)
lb2_fr1.grid(row=3,column=0,padx= 1, pady=10)
lb3_fr1.grid(row=4,column=0,padx= 1, pady=10)
in2_fr1.grid(row=4,column=2,padx= 1, pady=10)
lb4_fr1.grid(row=5,column=0,padx= 1, pady=10)
in3_fr1.grid(row=5,column=2,padx= 1, pady=10)
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
bt3_fr1.grid(row=8,column=0,padx=2, pady=10)
bt4_fr1.grid(row=8,column=2,padx=2, pady=10)



#fr1.pack()
#fr2.pack()
fr3.grid(row=0,column=4)



root.mainloop()

