#4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:

funcionarios = {'nome': 'Renato', 'idade': 14, 'cidade': 'São Paulo'}

if 'nome' in funcionarios:
    print("A chave 'nome' existe no dicionário")
else:
    print("A chave 'nome' não existe no dicionário")