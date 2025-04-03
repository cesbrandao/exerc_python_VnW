'''
Escreva uma função que recebe uma string e retorna um dicionário onde as chaves são os
caracteres da string e os valores representam quantas vezes cada caractere aparece.

Exemplo: ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

Saída: {'Java': 2, 'Ruby': 2, 'Javascript': 1}
'''

lista = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

def conta_frequencia(lista):
    frequencia = {}
    for elemento in lista:
        if elemento in frequencia:
            frequencia[elemento] += 1
        else:
            frequencia[elemento] = 1
    return frequencia

print(conta_frequencia(lista))