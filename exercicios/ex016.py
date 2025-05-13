n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opção = int(input('Qual a opção escolhida? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif opção == 3:
        maior = n1 if n1 > n2 else n2
        print('O número {} é maior que {}'.format(n1, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        print('Saindo do programa...')
    else:
        print('Opção invalida! Tente novamente.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
print('Fim do programa')