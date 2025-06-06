#importando depedencias do TKinter
from email.utils import collapse_rfc2231_value
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando aba view
from view import *

#cores
cor0 = '#2e2d2b' #preto
cor1 = '#feffff' #branco
cor2 = '#6b6968' #grey
cor3 = '#032e02' #verde
cor4 = '#403d3d' #letra
cor5 = '#003452' #azul
cor6 = '#ef5350' #vermelho
cor7 = '#038cfc' #azul
cor8 = '#263238' #azul escuro
cor9 = '#feffff' #branco
cor10 = '#db882e'

#criando janela
janela = Tk()
janela.title("")
janela.geometry("850x620")
janela.configure(background=cor1)
janela.resizable(width=False, height=FALSE)

style = Style(janela)
style.theme_use('clam')

#criando frames
frame_logo = Frame(janela, width = 850, height = 52, bg=cor5)
frame_logo.grid(row = 0, column = 0, pady = 0, padx = 0, sticky = NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row = 1, columnspan = 1, ipadx = 680)

frame_dados = Frame(janela, width = 850, height = 65, bg=cor1)
frame_dados.grid(row = 2, column = 0, pady = 0, padx = 0, sticky = NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row = 3, columnspan = 1, ipadx = 680)

frame_detalhes = Frame(janela, width = 850, height = 200, bg=cor1)
frame_detalhes.grid(row = 4, column = 0, pady = 0, padx = 10, sticky = NSEW)

frame_tabela = Frame(janela, width = 850, height = 200, bg=cor1)
frame_tabela.grid(row = 5, column = 0, pady = 0, padx = 10, sticky = NSEW)

#-----------trabalhando no frame logo-----------
app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text='Cadastro de Alunos', width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=cor5, fg=cor1)
app_logo.place(x=0, y=0)

#função para cadastrar alunos
def alunos():

    #criando campos de entrada
    I_nome = Label(frame_detalhes, text="Nome*", height = 1, anchor = NW, font = ('Ivy 10'), bg=cor1, fg=cor4)
    I_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify='left', relief = 'solid')
    e_nome.place(x=7, y=40)

    I_email = Label(frame_detalhes, text = "Email*", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_email.place(x = 4, y = 70)
    e_email = Entry(frame_detalhes, width = 45, justify = 'left', relief = 'solid')
    e_email.place(x = 7, y = 100)

    I_Contato = Label(frame_detalhes, text = "Contato*", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_Contato.place(x = 4, y = 130)
    e_Contato = Entry(frame_detalhes, width = 20, justify = 'left', relief = 'solid')
    e_Contato.place(x = 7, y = 160)

    I_sexo = Label(frame_detalhes, text = "Sexo*", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_sexo.place(x = 190, y = 130)
    c_sexo = ttk.Combobox(frame_detalhes, width = 12, font = ('Ivy 8 bold'))
    c_sexo['values'] = ('Masculino', 'Feminino')
    c_sexo.place(x = 190, y = 160)

    I_data_nascimento = Label(frame_detalhes, text='Data de nascimento*',height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_data_nascimento.place(x = 446, y = 10)
    data_nascimento = DateEntry(frame_detalhes, width = 18, background = 'darkblue', foreground = 'white', borderwidth = 2, year=2025)
    data_nascimento.place(x = 450, y = 40)

    I_cpf = Label(frame_detalhes, text = "CPF*", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_cpf.place(x = 446, y = 70)
    e_cpf = Entry(frame_detalhes, width = 22, justify = 'left', relief = 'solid')
    e_cpf.place(x = 450, y = 100)

    turmas = ['Turma A', 'Turma B']
    turma = []

    for i in turmas:
        turma.append(i)

    I_turma = Label(frame_detalhes, text = "Turma*", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_turma.place(x = 446, y = 130)
    c_turma = ttk.Combobox(frame_detalhes, width = 20, font = ('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x = 450, y = 160)

    #função para escolher imagem
    global imagem, imagem_string, I_imagem

    def escolher_imagem():
        global imagem, imagem_string, I_imagem

        imagem = fd.askopenfilename()
        imagem_string = imagem

        #abrindo imagem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        I_imagem = Label(frame_detalhes, image = imagem, bg = cor1, fg = cor4)
        I_imagem.place(x = 300, y = 10)

        botao_carregar['text'] = 'Trocar de foto'

    botao_carregar = Button(frame_detalhes, command = escolher_imagem, text = "CARREGAR FOTO ", width = 20, compound = CENTER, ancho=CENTER, overrelief = RIDGE, relief = RAISED, font=('Ivy 7'), bg=cor1, fg=cor0)
    botao_carregar.place(x = 300, y = 160)

    #linha separatoria
    I_linha = Label(frame_detalhes, relief = GROOVE, text='h', width = 1, height = 92, anchor = NW, font = ('Ivy 1'), bg=cor0, fg=cor0)
    I_linha.place(x = 610, y = 10)
    I_linha = Label(frame_detalhes, relief = GROOVE, text='h', width = 1, height = 92, anchor = NW, font = ('Ivy 1'), bg=cor1, fg=cor0)
    I_linha.place(x = 608, y = 10)

    #procuara aluno
    I_nome = Label(frame_detalhes, text = 'Procurar Alunos [ Entra o nome ]', height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg=cor4)
    I_nome.place(x = 627, y = 10)
    e_nome = Entry(frame_detalhes, width = 17, justify = 'center', relief = SOLID,font = ('Ivy 10'))
    e_nome.place(x = 630, y = 35)

    botao_procurar = Button(frame_detalhes, anchor = 'center', text = 'Procurar', width = 9, overrelief = 'ridge', font = ('Ivy 7'), bg=cor1, fg=cor0)
    botao_procurar.place(x = 757, y = 35)

    botao_salvar = Button(frame_detalhes, text="Salvar".upper(), anchor=CENTER, width = 9, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor7, fg=cor1)
    botao_salvar.place(x=627, y=110)

    botao_atualizar = Button(frame_detalhes, text="Atualizar".upper(), anchor=CENTER, width = 9, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor10, fg=cor1)
    botao_atualizar.place(x=627, y=135)

    botao_deletar = Button(frame_detalhes, text="Deletar".upper(), anchor=CENTER, width = 9, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor6, fg=cor1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, text="Ver".upper(), anchor=CENTER, width = 9, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor2, fg=cor1)
    botao_ver.place(x=727, y=160)

    def mostrar_alunos():
        app_nome = Label(frame_tabela, text = "Tabela de Alunos", height = 1, pady = 0, padx = 0, relief = "flat", anchor = NW, font = ('Ivy 10 bold'), bg = cor1, fg = cor4)
        app_nome.grid(row = 0, column = 0, padx = 0, pady = 10, sticky = NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID', 'Nome', 'Email', 'Contato', 'Sexo', 'Imagem', 'Data', 'CPF', 'Curso']
        df_list = []

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode = "extended", columns = list_header, show = "headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient = "vertical", command = tree_aluno.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient = "horizontal", command = tree_aluno.xview)

        tree_aluno.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
        tree_aluno.grid(column = 0, row = 1, sticky = 'nsew')
        vsb.grid(column = 1, row = 1, sticky = 'ns')
        hsb.grid(column = 0, row = 2, sticky = 'ew')
        frame_tabela.grid_rowconfigure(0, weight = 12)

        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
        h = [40,150,150,70,70,70,80,80,100]
        n = 0

        for col in list_header:
            tree_aluno.heading(col, text = col.title(), anchor = NW)
            #adjust the column's width to the header string
            tree_aluno.column(col, width = h[n], anchor = hd[n])

            n += 1

        for item in df_list:
            tree_aluno.insert('', 'end', values = item)

    mostrar_alunos()

#função para adicionar cursos e turmas
def adicionar():
    # criando frame para tabelas
    frame_tabela_curso = Frame(frame_tabela, width = 300, height = 200, bg = cor1)
    frame_tabela_curso.grid(row = 0, column = 0, pady = 0, padx = 10, sticky = NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30,height=200, bg=cor1)
    frame_tabela_linha.grid(row = 0, column = 1, pady = 0, padx = 10, sticky = NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300,height=200, bg=cor1)
    frame_tabela_turma.grid(row = 0, column = 2, pady = 0, padx = 10, sticky = NSEW)

    #detalhes do curso
    #funçao novo curso
    def novo_curso():
        nome = e_nomecurso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()

        lista = [nome, duracao, preco]

        #verificando se os valores estao vazios
        for i in lista:
            if i == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

        # inserindo os dados
        criar_curso(lista)
        messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso.')

        e_nomecurso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)

        mostrar_cursos()

    # funçao atualizar curso
    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nomecurso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])

            #funçao atualizar
            def update():

                nome = e_nomecurso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()

                lista = [nome, duracao, preco, valor_id]

                # verificando se os valores estao vazios
                for i in lista:
                    if i == "":
                        messagebox.showerror("Erro", "Preencha todos os campos.")
                        return

                # inserindo os dados
                atualizar_curso(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso.')

                e_nomecurso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)

                mostrar_cursos()

                #destruindo o botao salvar apos salvar os dados
                botao_salvar.destroy()

            botao_salvar = Button(frame_tabela, command=update, anchor='center', text="Salvar atualização".upper(), overrelief = 'ridge', font = ('Ivy 7 bold'), bg = cor3, fg = cor1)
            botao_salvar.place(x=180, y=160)

        except IndexError:
            messagebox.showerror('Erro', 'Selecionar um dos cursos na tabela')

    I_nome = Label(frame_detalhes, text="Nome do Curso", height = 1, anchor = NW, font = ('Ivy 10'), bg=cor1, fg=cor4)
    I_nome.place(x=4, y=10)
    e_nomecurso = Entry(frame_detalhes, width=35, justify='left', relief = 'solid')
    e_nomecurso.place(x=7, y=40)

    I_duracao = Label(frame_detalhes, text="Duração", height = 1, anchor = NW, font = ('Ivy 10'), bg=cor1, fg=cor4)
    I_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief = 'solid')
    e_duracao.place(x=7, y=100)

    I_preco = Label(frame_detalhes, text="Preço", height = 1, anchor = NW, font = ('Ivy 10'), bg=cor1, fg=cor4)
    I_preco.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify='left', relief = 'solid')
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, command=novo_curso,  anchor=CENTER, text="Salvar".upper(),  width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor7, fg=cor1)
    botao_carregar.place(x=100, y=160)

    botao_atualizar = Button(frame_detalhes, command = update_curso, text="Atualizar".upper(), anchor=CENTER, width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor10, fg=cor1)
    botao_atualizar.place(x=180, y=160)

    botao_deletar = Button(frame_detalhes, text="Deletar".upper(), anchor=CENTER, width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor6, fg=cor1)
    botao_deletar.place(x=260, y=160)

    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text = "Tabela de Cursos", height = 1, pady = 0, padx = 0, relief = "flat", anchor = NW, font = ('Ivy 10 bold'), bg = cor1, fg = cor4)
        app_nome.grid(row = 0, column = 0, padx = 0, pady = 10, sticky = NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID', 'Curso', 'Duração', 'Preço']
        df_list = ver_cursos()

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode = "extended", columns = list_header, show = "headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient = "vertical", command = tree_curso.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient = "horizontal", command = tree_curso.xview)

        tree_curso.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
        tree_curso.grid(column = 0, row = 1, sticky = 'nsew')
        vsb.grid(column = 1, row = 1, sticky = 'ns')
        hsb.grid(column = 0, row = 2, sticky = 'ew')
        frame_tabela_curso.grid_rowconfigure(0, weight = 12)

        hd = ["nw", "nw", "e", "e"]
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            tree_curso.heading(col, text = col.title(), anchor = NW)
            #adjust the column's width to the header string
            tree_curso.column(col, width = h[n], anchor = hd[n])

            n += 1

        for item in df_list:
            tree_curso.insert('', 'end', values = item)

    mostrar_cursos()

    #linha separatoria
    I_linha = Label(frame_detalhes, relief = GROOVE, text='h', width = 1, height = 92, anchor = NW, font = ('Ivy 1'), bg=cor0, fg=cor0)
    I_linha.place(x = 375, y = 10)
    I_linha = Label(frame_detalhes, relief = GROOVE, text='h', width = 1, height = 92, anchor = NW, font = ('Ivy 1'), bg=cor1, fg=cor0)
    I_linha.place(x = 373, y = 10)

    # linha separatoria tabela
    I_linha = Label(frame_tabela_linha, relief = GROOVE, text = 'h', width = 1, height = 105, anchor = NW, font = ('Ivy 1'), bg = cor0, fg = cor0)
    I_linha.place(x = 7, y = 50)
    I_linha = Label(frame_tabela_linha, relief = GROOVE, text = 'h', width = 1, height = 105, anchor = NW, font = ('Ivy 1'), bg = cor1, fg = cor0)
    I_linha.place(x = 5, y = 50)

    #detalhes da turma
    I_nome = Label(frame_detalhes, text = "Nome da Turma", height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_nome.place(x = 404, y = 10)
    e_nome_turma = Entry(frame_detalhes, width = 35, justify = 'left', relief = 'solid')
    e_nome_turma.place(x = 407, y = 40)

    I_turma = Label(frame_detalhes, text='Turma', height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_turma.place(x = 404, y = 70)

    #pegando os cursos
    cursos = ['curso 1', 'curso 2']
    curso = []

    for i in cursos:
        curso.append(i)

    c_curso = ttk.Combobox(frame_detalhes, width = 20, font = ('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x = 407, y = 100)

    I_data_inicio = Label(frame_detalhes, text='Data de Início',height = 1, anchor = NW, font = ('Ivy 10'), bg = cor1, fg = cor4)
    I_data_inicio.place(x = 406, y = 130)
    data_inicio = DateEntry(frame_detalhes, width = 10, background = 'darkblue', foreground = 'white', borderwidth = 2, year=2025)
    data_inicio.place(x = 407, y = 160)

    botao_carregar = Button(frame_detalhes, text="Salvar".upper(), anchor=CENTER, width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor7, fg=cor1)
    botao_carregar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes, text="Atualizar".upper(), anchor=CENTER, width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor10, fg=cor1)
    botao_atualizar.place(x=587, y=160)

    botao_deletar = Button(frame_detalhes, text="Deletar".upper(), anchor=CENTER, width = 10, overrelief = RIDGE, font = ('Ivy 7 bold'), bg=cor6, fg=cor1)
    botao_deletar.place(x=667, y=160)

    # tabela turmas
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text = "Tabela de Turmas", height = 1, pady = 0, padx = 0, relief = "flat", anchor = NW, font = ('Ivy 10 bold'), bg = cor1, fg = cor4)
        app_nome.grid(row = 0, column = 0, padx = 0, pady = 10, sticky = NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID', 'Nome da Turma', 'Curso', 'Inicio']
        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode = "extended", columns = list_header, show = "headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient = "vertical", command = tree_turma.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient = "horizontal", command = tree_turma.xview)

        tree_turma.configure(yscrollcommand = vsb.set, xscrollcommand = hsb.set)
        tree_turma.grid(column = 0, row = 1, sticky = 'nsew')
        vsb.grid(column = 1, row = 1, sticky = 'ns')
        hsb.grid(column = 0, row = 2, sticky = 'ew')
        frame_tabela_turma.grid_rowconfigure(0, weight = 12)

        hd = ["nw", "nw", "e", "e"]
        h = [30, 130, 150, 80]
        n = 0

        for col in list_header:
            tree_turma.heading(col, text = col.title(), anchor = NW)
            #adjust the column's width to the header string
            tree_turma.column(col, width = h[n], anchor = hd[n])

            n += 1

        for item in df_list:
            tree_turma.insert('', 'end', values = item)

    mostrar_turmas()


#função para salvar
def salvar():
    print('Salvar')

# -----------funçao de controles-----------
def control(i):
    #cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a função alunos
        alunos()

    #cadastro de adicionar
    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a função adicionar
        adicionar()

    #cadastro de aluno
    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        #chamando a função salvar
        salvar()

#criando botoes
app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text='Cadastro', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
app_cadastro.place(x=10, y=30)

app_img_adiciona = Image.open('add.png')
app_img_adiciona = app_img_adiciona.resize((18,18))
app_img_adiciona = ImageTk.PhotoImage(app_img_adiciona)
app_adiciona = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adiciona, text='Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
app_adiciona.place(x=123, y=30)

app_img_salvar = Image.open('salvar.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text='Salvar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=cor1, fg=cor0)
app_salvar.place(x=236, y=30)




alunos() #ja pra iniciar o programa na aba cadastro
janela.mainloop()
