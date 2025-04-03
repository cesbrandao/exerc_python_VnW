'''
Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
pode ser lida da mesma forma de trás para frente) e False caso contrário.

Exemplo:
entrada = "radar"

Saída: True
'''

def verifica_palindromo(palavra):
    
    # palavra[::-1] reverte a string e valida se é igual a original
    return palavra == palavra[::-1]

print(verifica_palindromo("radar"))
print(verifica_palindromo("python"))