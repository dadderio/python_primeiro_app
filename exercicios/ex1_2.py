#EXERCICIO 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
#para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input('Digite a sua idade: \n'))
if 0 <= idade <= 12:
    print(f'A idade digitada é {idade}. Categoria "criança"')
elif 13 <= idade <= 18:
    print(f'A idade digitada é {idade}. Categoria "adolescente"')
elif idade > 18:
    print(f'A idade digitada é {idade}. Categoria "adulto"')
else:
    print('Número menor que 0 não se enquadra em nenhuma categoria')