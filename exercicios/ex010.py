velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Você está acima da velocidade permitido!')
    multa = (velocidade-80) * 7
    print('Sua multa é de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')