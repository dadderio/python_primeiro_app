#5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    
print(contagem_palavras)