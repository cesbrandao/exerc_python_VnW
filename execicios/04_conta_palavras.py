'''
Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.

Exemplo: ["banana maçã banana laranja maçã maçã"]

Saída: {"banana": 2, "maçã": 3, "laranja": 1}
'''

string = "banana maçã banana laranja maçã maçã"

def conta_palavras(string):
    
    # split() divide a string em palavras e retorna uma lista
    palavras = string.split()
    # print(palavras)
    
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

print(conta_palavras(string))