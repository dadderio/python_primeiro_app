from datetime import date

#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;

numeros=[]
for i in range (1,11):
  numeros.append(i)
print('lista de números: ',numeros)

#Lista com quatro nomes;

lista_com_quatro_nomes=[]
for _ in range (4):
  nome = input('Digite um nome: ')
  lista_com_quatro_nomes.append(nome)
print('Lista com quatro nomes: ', lista_com_quatro_nomes)


#Lista com o ano que você nasceu e o ano atual.
#from datetime import date

lista_de_anos=[]
idade = int(input('Digite a sua idade: '))
ano_atual = date.today().year
print(f'Você nasceu em: {ano_atual - idade}')
ano_nascimento = ano_atual -  idade
lista_de_anos.append([ano_nascimento, ano_atual])
print(lista_de_anos)

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

animais = ['cachorro', 'gato', 'macaco', 'girafa']

for animal in animais:
  print('Animal: ', animal)


#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma_impares = 0 
for i in range(1,11):
  if i % 2 != 0:
    soma_impares += i
print('A soma dos números ímpares de 1 e 10: ',soma_impares)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
  print ('Os números de 1 a 10 em ordem decrescente: ', i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for 
# para imprimir a tabuada desse número, indo de 1 a 10.
  
numero = int(input('Digite um número: '))
print('Número digitado: ', numero)
for i in range(1,11):
  print(f'{i} x {numero} = {i * numero}')

# 7 - Construa um código que calcule a média dos valores em uma lista.
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.