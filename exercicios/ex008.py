nome = str(input('Qual seu nome? '))
if nome == 'Jhonata':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Lucas' or nome == 'Maria':
    print('Esse nome é bem popular no Brasil!')
elif nome in 'Ana Jessica Julia':
    print('Nome feminino.')
else:
    print('Faz tempo que não escuto este nome.')
print('Bom dia, {}!'.format(nome))

# só o if é uma condicional simples, com else é condicional composta