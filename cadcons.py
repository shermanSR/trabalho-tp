from salvler import *
from random import randint

def consultar():
    catalogo = lercatg()
    for i in catalogo:
        placa = i['Placa']
        marcas = i['Marca']
        modelos = i['Modelo']
        ano = i['Ano']
        cor = i['Cor']
        cambio = i['Cambio']
        print(f'A Placa do Veículo é: {placa}')
        print(f'A Marca Do Veículo é: {marcas}')
        print(f'O Modelo do Veículo é: {modelos}')
        print(f'O Ano do Veículo é: {ano}')
        print(f'A Cor do Veículo é: {cor}')
        print(f'O Câmbio do Veículo é: {cambio}')
        print(25 * '-')


def cadveiculo() :
    veículos = {}
    veículos['Placa'] = randint(100,1000)
    veículos['Marca'] = str(input('Digite a Marca do Veículo: '))
    veículos['Modelo'] = str(input('Digite o Modelo do Veículo: '))
    veículos['Ano'] = int(input('Digite o Ano do Veículo: '))
    veículos['Cor'] = str(input('Digite a Cor do Veículo: '))
    veículos['Cambio'] = str(input('Digite o tipo de o Câmbio: '))
    catag = lercatg()
    catag.append(veículos)
    salvarcatag(catag)