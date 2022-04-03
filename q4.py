from typing import List
#4)	Construa um programa utilizando uma pilha que resolva o seguinte problema:
#Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita.
#Dado uma placa verifique se o carro está estacionado na rua. Caso esteja, informe a sequência de carros que deverá
#ser retirada para que o carro em questão consiga sair.

def main():
    stack: List[int] = [1015, 1014, 1013, 1012, 1011]
    placa = 1015
    print('Sequência de carros para ser retirados ' +  str(conseguir_sair(stack, placa)))

def conseguir_sair(stack, placa):
    carros_para_retirar: List[int] = []
    for element in stack[::-1]:
        if element != placa:
            carros_para_retirar.append(element)
        elif element == placa:
            return carros_para_retirar

    return 'Não existe nenhum carro com essa placa'

main()
