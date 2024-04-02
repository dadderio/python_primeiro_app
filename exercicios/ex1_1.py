#EXERCICIO 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input('Digite um número: \n'))
if numero%2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

