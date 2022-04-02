# 1)	Escrever uma função que receba como parâmetro uma pilha.
# A função deve retornar o maior elemento da pilha. A passagem deve ser por valor ou referência?
from typing import List

def main():
    pilha: List[int] = [1, 2, 3, 4, 5] # Referência na memória , valor -> 1,2,3,4,5
    print('Maior elemento da pilha ' + str(recebe_pilha(pilha)))

def recebe_pilha(stack):
    #LIFO -> Last in first out
    maior_elemento = 0
    for element in stack[::-1]:
        if element > maior_elemento:
            maior_elemento = element
    return maior_elemento

main()