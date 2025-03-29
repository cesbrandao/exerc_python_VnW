'''
Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.

Exemplo: ("Samuel", "Karynne", "Carol", "Kleber", "Vinicius")

Saída: ("Carol", "Karynne", "Kleber", "Samuel", "Vinicius")
'''

# tupla = ("Samuel", "Karynne", "Carol", "Kleber", "Vinicius")

tupla = [
    ("Samuel", 30),
    ("Karynne", 25),
    ("Carol", 28),
    ("Kleber", 35),
    ("Vinicius", 22)
    ]

def ordena_tupla(tupla):
    # Ordena a lista de tuplas pela idade (segundo elemento da tupla)
    return sorted(tupla, key=lambda x: x[1])

print(ordena_tupla(tupla))