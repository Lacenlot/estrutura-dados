from typing import List
#2)	Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

def main():
    pilhaUm: List[int] = [1, 2, 3, 4, 5]
    pilhaDois: List[int] = [1, 2, 3, 4, 5]
    print(recebe_duas_pilhas(pilhaUm, pilhaDois))

def recebe_duas_pilhas(pilhaUm, pilhaDois):
    #LIFO
    #length -> tamanho = len()
    qtdItensPUm = len(pilhaUm)
    qtdItensPDois =  len(pilhaDois)

    if qtdItensPUm != qtdItensPDois:
        return 'As pilhas tem tamanho diferente!'

    for elementoUm, elementoDois in zip(pilhaUm, pilhaDois)[::-1]:
        if elementoUm != elementoDois:
            return 'As Pilhas são diferentes!'

    return 'As pilhas são iguais'

main()
