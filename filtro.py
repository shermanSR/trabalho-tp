from salvler import *

def opcoes():
    print('Essas são as nossas opções de filtro.')
    print('Atraves da Placa.')
    print('Atraves da Marca.')
    print('Atraves do Modelo.')
    print('Atraves do Ano.')
    print('Atraves da Cor.')
    print('Atraves do Câmbio.')
    print(25 * '-')
    filtro = input('Digite a opção de pesquisa: ')
    escolha = input('Digite oque deseja filtrar: ')
    catalogo = lercatg()
    for i in catalogo:
        if i[filtro] == escolha:
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