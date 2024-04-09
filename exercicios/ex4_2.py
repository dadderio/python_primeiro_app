funcionarios = {'nome': 'Renato', 'idade': 14, 'cidade': 'São Paulo'}

print(f'\n Nome do funcionário: {funcionarios.get('nome')}\n')


print('a)modifique a idade da pessoa:\n')
#funcionarios.update({'idade':13})
funcionarios['idade']=13
#print(funcionarios.get('idade'))
print(funcionarios['idade'],'\n')

print('b)adicione um campo de profissão para essa pessoa:\n')
funcionarios.update({'profissão':'estudante'})
print(funcionarios['profissão'],'\n')
print(funcionarios,'\n')

print('\nc)Remova um item do dicionário:\n')
#del funcionarios['profissão']
item_removido = funcionarios.pop('profissão')
print(item_removido,'\n')
print(funcionarios,'\n')