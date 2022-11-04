import os
from altexcl import *
from cadcons import *
from filtro import *

while True:
    os.system('cls')
    print(25 * '-')
    print('Bem Vindo a ES Veículos')
    print(25 * '-')
    print('1 - Cadastrar Veículos') 
    print('2 - Consultar Inventario')
    print('3 - Consultar por Filtro')
    print('4 - Alterar Inventario')
    print('5 - Excluir Veículo')
    print(25 * '-')

    escolha = int(input("Insira a opção desejada: "))
    if escolha == 1:
        cadveiculo()
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        if parar == 'x':
            break
    elif escolha == 2:
        consultar()
        print(25 * '-')
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        if parar == 'x':
            break
    elif escolha == 3:
        opcoes()
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        if parar == 'x':
            break
    elif escolha == 4:
        alterar()
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        if parar == 'x':
            break
    elif escolha == 5:
        excluir()
        parar = input('Caso Deseje Encerrar o Programa Digite x: ')
        if parar == 'x':
            break

