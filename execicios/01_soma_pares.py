'''
Primeiro Exercício: Soma de elementos pares

Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
elementos pares contidos nela.

Exemplo: [2,4,10,3,9,7,15,22]

Saída: A soma dos pares é: x
'''

lista = [2, 4, 10, 3, 9, 7, 15, 22]

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

print(f'A soma dos pares é: {soma_pares(lista)}')