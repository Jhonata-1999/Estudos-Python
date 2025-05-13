n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor {}'.format(n, (n-1), (n+1)))

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))
# \n serve para quebra de linha
# :.2f serve para mostrar duas casas após o .