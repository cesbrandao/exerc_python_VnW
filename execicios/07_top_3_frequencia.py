'''
Dada uma lista de números, crie uma função que retorne os três números mais frequentes
em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.

Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

Saída: [2, 1, 4]
'''

lista_num = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

def top_3_frequencia(lista):
    frequencias = {}
    #cria um dicionário com as frequências dos números {numero: frequencia}
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    
    print(frequencias)
    
    # A função sorted retorna uma lista de tuplas (numero, frequencia) ordenadas
    # Primeiro pela frequência (em ordem decrescente -x[1]) e depois (em caso de empate) pelo número (em ordem crescente x[0])
    numeros_ordenados = sorted(frequencias.items(), key=lambda x: (-x[1], x[0]))
    
    print(numeros_ordenados)
    
    # Extrai os três primeiros números
    top_3 = [num for num, freq in numeros_ordenados[:3]]
    
    return top_3

print(top_3_frequencia(lista_num))