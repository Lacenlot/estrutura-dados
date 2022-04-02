from typing import List
#7)	Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um:
#- se positivo, inserir na pilha P; #2
#- se negativo, inserir na pilha N; #1
#- se zero, retirar um elemento de cada pilha.

def main():
    pilhaPositivos: List[int] = []
    pilhaNegativos: List[int] = []
    vector = [1,2, -1, -2, 0, 3, -3]
    TPilha2(pilhaNegativos, pilhaPositivos, vector)

def TPilha2(pilhaNegativos, pilhaPositivos, vector):
    for elemento in vector[::-1]:
        if elemento > 0:
            pilhaPositivos.append(elemento)
        elif elemento < 0:
            pilhaNegativos.append(elemento)
        else:
            pilhaNegativos.pop()
            pilhaPositivos.pop()

    print(pilhaNegativos)
    print(pilhaPositivos)

main()