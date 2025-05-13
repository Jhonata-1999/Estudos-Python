distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
#if distancia <= 200:
#    preco = distancia * 0.50
#else:
#    preco = distancia * 0.45
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #simplificado
print('O preço da passagem será de R$ {:.2f}'.format(preco))