import sqlite3

try:

    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE nome = '+nome+'")

    banco.commit()

    banco.close()
    print('Os dados foram remoridos com sucesso!')

except sqlite3.Error as erro:
    print('Erro ao excluir: ',erro)