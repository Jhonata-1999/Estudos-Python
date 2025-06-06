import sqlite3

# criar conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conectado ao banco de dados.')
except sqlite3.Error as e:
    print('Erro na conexão: ', e)

# criar tabela de cursos
try:
    with con:
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                duracao TEXT,
                preco REAL
        )""")

        print('Tabela cursos criada com sucesso.')

except sqlite3.Error as e:
    print('Erro ao criar tabela: ')

# criar tabela de turmas
try:
    with con:
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                curso_nome TEXT,
                data_inicio DATE,
                FOREIGN KEY(curso_nome) REFERENCES cursos(nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")

        print('Tabela turmas criada com sucesso.')

except sqlite3.Error as e:
    print('Erro ao criar turmas: ')

# criar tabela de alunos
try:
    with con:
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                contato TEXT,
                sexo TEXT,
                imagem TEXT,
                data_nascimento DATE,
                cpf TEXT,
                turma_nome TEXT,
                FOREIGN KEY (turma_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")

        print('Tabela alunos criada com sucesso.')

except sqlite3.Error as e:
    print('Erro ao criar alunos: ')

