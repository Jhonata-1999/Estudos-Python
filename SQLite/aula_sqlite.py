import sqlite3

nome = "Isis"
idade = 18
email = "isis@email.com"

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

# CRIAR TABELA
#cursor.execute('CREATE TABLE pessoas (nome text,idade integer, email text)')

# INSERIR DADOS (USANDO CONCATENAÇÃO DE STRINGS)
#cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"','"+str(idade)+"','"+email+"')")

# INSERIR DADOS COM FUNÇÃO VERIFICAR ANTES (USANDO PLACEHOLDER)
cursor.execute("SELECT * FROM pessoas WHERE email = ?", (email,))
registro_existente = cursor.fetchone()

if registro_existente:
    print("Erro: O email já está cadastrado no banco de dados.")
else:
    cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
    banco.commit()
    print("Usuário cadastrado com sucesso!")

# SEMPRE FINALIZAR OM COMMIT
#banco.commit()

#cursor.execute("SELECT * FROM pessoas")

#print(cursor.fetchall())