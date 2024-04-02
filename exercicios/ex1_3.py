#EXERCICIO 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else 
#para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario_correto = "python"
senha_correta= "python3"

usuario = input('Digite o seu nome \n')
senha = input('Digite a senha \n')

if usuario == usuario_correto and senha == senha_correta:
    print('Login bem sucedido')
else:
    print('Credenciais inválidas. Tente novamente!')