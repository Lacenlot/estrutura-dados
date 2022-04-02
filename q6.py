from typing import List
#6)	Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue:
#- se o número for par, insira-o na pilha;
#- se o número lido for ímpar, retire um número da pilha;
#- Ao final, esvazie a pilha imprimindo os elementos.

def main():
    vector = [4,2,3,4,5,6,7,8,9,22,11,12,13,14,18]
    TPilha(vector)

def TPilha(vector):
    if len(vector) < 15:
        return 'O vetor possui um tamanho inválido'

    stack: List[int] = []

    for element in vector[::-1]:
        if (element % 2) == 0:
            stack.append(element)
        else:
           if len(stack) > 0:
               stack.pop()

    for i in range(len(stack)): #TAMANHO
        i = 0 #TOPO
        if len(stack) > 0:
            print(stack.pop(i))

    print(stack)

main()