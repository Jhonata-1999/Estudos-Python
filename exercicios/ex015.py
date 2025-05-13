# while é o "enquanto", os comandos são baseados no "enquanto não..." "se..." quando o enquanto for falso, finaliza a ação.


# r = 'S'
# while r == 'S': #enquanto a resposta for diferente de S o programa continua
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')


# n = 1
# while n != 0: #enquanto a numero for diferente de 0 o programa continua
#     n = int(input('Digite um valor: '))
# print('FIM')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #este teste vai funcionar somente se for diferente de 0
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares'.format(par, impar))