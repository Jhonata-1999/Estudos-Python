print('{:^40}'.format('LOJAS JHONSON'))
preco = float(input('Preço das compras: R$ '))
print(""""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais""")
opcao = input('Qual a opção? ')
if opcao == '1':
    total = preco - (preco * 0.1)
elif opcao == '2':
    total = preco - (preco * 0.005)
elif opcao == '3':
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x SEM JUROS de R$ {:.2f}'.format(parcela))
elif opcao == '4':
    total = preco + (preco * 0.2)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x COM JUROS de R$ {:.2f}'.format(totalparc, parcela))
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, total))
