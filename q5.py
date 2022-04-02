from typing import List
#5)	Utilizando uma pilha resolver o exercício a seguir:
#Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

def main():
    stack: List[int] = [1,2,3,4,5]
    imprimir_numeros_reais(stack)

def imprimir_numeros_reais(stack):
    for element in stack[::-1]:
        if element > 0:
            print(element)

main()
