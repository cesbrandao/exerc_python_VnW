'''
Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas
notas, crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do
aluno e sua média de notas.

Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}

Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]
'''

dicionario = {
    "Ana": [8, 9, 7],
    "Bruno": [5, 6, 5],
    "Carlos": [10, 9, 10]
}

def calcula_media(dicionario):
    medias = []
    for aluno, notas in dicionario.items():
        media = sum(notas) / len(notas)
        medias.append((aluno, round(media, 2)))
    return medias

print(calcula_media(dicionario))