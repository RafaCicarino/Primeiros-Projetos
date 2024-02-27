
from tkinter import *

janela = Tk()
janela.title("Calculando Médias da Materias")
janela.geometry("350x300")
janela.resizable(width=False, height=False)

# coletando dados

label1 = Label (janela, text = "Primeira nota")
label1.grid (column = 0, row = 1)
entrada1=(Entry(janela,width=10,justify=CENTER))
entrada1.grid(column=1, row=1)


label2 = Label (janela, text = "Segunda nota")
label2.grid (column = 0, row = 2)
entrada2 = Entry(janela,width=10,justify=CENTER)
entrada2.grid(column=1, row=2)


label3 = Label (janela, text = "Terceira nota")
label3.grid (column = 0, row = 3)
entrada3 = Entry(janela,width=10, justify=CENTER)
entrada3.grid(column=1, row=3,)


label4 = Label (janela, text = "Quarta Nota")
label4.grid (column = 0, row = 4)
entrada4 = Entry(janela,width=10, justify=CENTER)
entrada4.grid(column=1, row=4)



#definindo variaveis
def obter():
    nota1=float(entrada1.get())
    nota2=float(entrada2.get())
    nota3=float(entrada3.get())
    nota4=float(entrada4.get())
    somatorio=(int(nota1)+int(nota2)+int(nota3)+int(nota4))
    resultado=somatorio/4
    

    mostrar_na_tela["text"]=resultado
   
    
#criando botoes
texto_titulo=Label(janela, text="Digite as notas para calcular a media.\nAtento em colocar ponto no lugar de virgula", font=("calibri","12","bold"))
texto_titulo.grid(column=0, row=0,columnspan=2, padx=40, pady=5)


texto_resultado=Label(janela, text="Sua media foi")
texto_resultado.grid(column=0, row=10)

mostrar_na_tela=Label(janela, text="", font=("Calibri","16","bold"))
mostrar_na_tela.grid(column=0, row=12)


botao = Button(janela, fg='orange',text="Calcular a Media", font=("calibri","12","bold"),command=obter)
botao.grid(column=1, row=6)
botao.configure(borderwidth=0)




janela.mainloop()