import sqlite3

#criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com banco de dados: ', e)

#----------tabela de cursos----------

#criar cursos (Inserir C)
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i,)

#criar_curso(['Python','Semanas',50])

#ver todos os cursos (Selecionar R)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Cursos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista



#atualizar os cursos (Update U)
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome = ?, duracao = ?, preco = ? WHERE id = ?"
        cur.execute(query,i,)


#atualizar_curso(I)

#deletar cursos (Delete D)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id = ?"
        cur.execute(query,i,)

#deletar_curso([1])

#----------tabela de turmas----------
#criar turmas (Inserir C)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, cursos_nome, data_inicio) VALUES (?,?,?)"
        cur.execute(query,i,)

#ver todos as turmas (Selecionar R)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Turmas")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#atualizar as turmas (Update U)
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome = ?, cursos_nome = ?, data_inicio = ? WHERE id = ?"
        cur.execute(query,i,)

#deletar turmas (Delete D)
def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id = ?"
        cur.execute(query,i,)

#----------tabela de alunos----------
#criar alunos (Inserir C)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, emil, contato, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query,i,)

#ver todos os alunos (Selecionar R)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Alunos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#atualizar as alunos (Update U)
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Alunos SET nome = ?, emil = ?, contato = ?, sexo = ?, imagem = ?, data_nascimento = ?, cpf = ?, turma_nome = ? WHERE id = ?"
        cur.execute(query,i,)

#deletar alunos (Delete D)
def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id = ?"
        cur.execute(query,i,)
