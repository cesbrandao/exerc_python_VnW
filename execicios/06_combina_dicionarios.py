'''
Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são
inteiros. A função deve combinar os dicionários somando os valores das chaves que
aparecem em ambos.

Exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

Saída: {"a": 3, "b": 7, "c": 5, "d": 7}
'''

d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

def combina_dicionarios(d1, d2):
    dict_combinado = d1.copy()  # Cria uma cópia do primeiro dicionário
    for chave, valor in d2.items():
        if chave in dict_combinado:
            dict_combinado[chave] += valor
        else:
            dict_combinado[chave] = valor
    return dict_combinado

print(combina_dicionarios(d1, d2))