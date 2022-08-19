# importando tkinter
from tkinter import *

###############################
# DEFININDO INFO DO PROGRAMA
janela = Tk()
# NOME DO PROGRAMA
janela.title("Programa de Entradas")
# DIMENSSÃO DA TELA DO PROGRAMA
janela.geometry("450x300")
###############################






# CRIANDO FUNÇÕES
def obter_dado():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    #botão ver dados:
    label_nome_re["text"] = nome
    label_idade_re["text"] = idade
    label_pais_re["text"] = pais

    #botão apagar
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)













#CAMPOS NOME
###############################
#texto nome: nome = label(aplicação, largura, altura, texto, fonte="arial tamanho 10", cor="cor da letra.", bg="cor do background")
label_nome = Label(janela, width=10, height=2, text="Nome", font="Arial 10", fg='#fc3503')
# LABEL_NOME = (LINHA, COLUNA)
label_nome.grid(row=0, column=0, )

#criando caixa de entrada(nome_aplicação, largura, font('arial tamanho 10'))
entry_nome = Entry(janela, width=20, font=('Arial 10'))
#posição onde se encontrará a caixa de entrada(LINHA, COLUNA, POSIÇÃO EIXO-X, POSIÇÃO EIXO-Y
entry_nome.grid(row=0, column=2, padx=10, pady=5)
###############################




# CAMPOS IDADE
###############################
#texto nome: nome = label(aplicação, largura, altura, texto, fonte="arial tamanho 10", cor="cor da letra.", bg="cor do background")
label_idade = Label(janela, width=10, height=2, text="Idade", font="Arial 10", fg='#fc3503')
# LABEL_NOME = (LINHA, COLUNA)
label_idade.grid(row=1, column=0, )

#criando caixa de entrada(nome_aplicação, largura, font('arial tamanho 10'))
entry_idade = Entry(janela, width=20, font=('Arial 10'))
#posição onde se encontrará a caixa de entrada(LINHA, COLUNA, POSIÇÃO EIXO-X, POSIÇÃO EIXO-Y
entry_idade.grid(row=1, column=2, padx=10, pady=5)
###############################





# CAMPOS PAIS

#texto nome: nome = label(aplicação, largura, altura, texto, fonte="arial tamanho 10", cor="cor da letra.", bg="cor do background")
label_pais = Label(janela, width=10, height=2, text="Pais", font="Arial 10", fg='#fc3503')
# LABEL_NOME = (LINHA, COLUNA)
label_pais.grid(row=2, column=0, )

#criando caixa de entrada(nome_aplicação, largura, font('arial tamanho 10'))
entry_pais = Entry(janela, width=20, font=('Arial 10'))
#posição onde se encontrará a caixa de entrada(LINHA, COLUNA, POSIÇÃO EIXO-X, POSIÇÃO EIXO-Y
entry_pais.grid(row=2, column=2, padx=10, pady=5)
###############################








# RESPOSTAS

label_nome_re = Label(janela, width=10, height=2, text="", font=("Arial 10"))
label_nome_re.grid(row=0, column=3, padx=10, pady=5)


label_idade_re = Label(janela, width=10, height=2, text="", font=("Arial 10"))
label_idade_re.grid(row=1, column=3, padx=10, pady=5)


label_pais_re = Label(janela, width=10, height=2, text="", font=("Arial 10"))
label_pais_re.grid(row=2, column=3, padx=10, pady=5)











# CRIANDO BOTÃO VER DADOS
# botaão = Button(nome_da_aplicação, função_def_obter_dado, largura, altura, texto="Ver Dados", relief="raised", cor="black")
botao = Button(janela, command=obter_dado, width=10, height=1, text="Ver Dados", relief='raised', fg="black")
#botao.local(linha=3, coluna=2, eixo-x=5, eixo-y=10)
botao.grid(row=3, column=2, padx=5, pady=10)



# CRIANDO BOTÃO APAGAR



# LOOP PARA MOSTRAR APLICAÇÃO
janela.mainloop()
