from typing import List
#3)	Escreva uma função que preencha uma pilha passada como parâmetro
# com os elementos de um vetor passado como parâmetro

def main():
    stack: List[int] = []
    vector = [1, 2, 3, 4, 5]
    pilha_com_vetor(stack, vector)

def pilha_com_vetor(stack, vector):
    for elemento in vector[::-1]:
        stack.append(elemento)

    print(stack)


main()