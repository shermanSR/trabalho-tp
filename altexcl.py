from salvler import *

def alterar():
    catalogo = lercatg()
    print(25 * '-')
    placa = int(input('digite a Placa do veículo: '))
    print(25 * '-')
    while True:
        for i in catalogo:
            if placa == i['Placa']:
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
                escolha = input('Digite qual Informação você deseja Alterar: ')
                print(25 * '-')
                escolha = escolha.upper()
                if escolha == 'MARCA':
                    i['Marca'] = input('Digite a Nova Marca do Veículo: ')
                    print(25 * '-')
                if escolha == 'MODELO':
                    i['Modelo'] = input('Digite o novo Modelo do Veículo: ')
                    print(25 * '-')
                if escolha == 'ANO':
                    i['Ano'] = int(input('Digite o novo Ano do Veículo: '))
                    print(25 * '-')
                if escolha == 'COR':
                    i['Cor'] = input('Digite a Nova Cor do Veículo: ')
                    print(25 * '-')
                if escolha == 'CAMBIO':
                    i['Cambio'] = input('Digite o novo tipo de Câmbio do Veículo: ')
                    print(25 * '-')
                if escolha == 'CÂMBIO':
                    i['Cambio'] = input('Digite o novo tipo de Câmbio do Veículo: ')
                    print(25 * '-')   
        salvarcatag(catalogo)
        continuar = input('Deseja editar mais alguma Informação? S/N: ')
        continuar = continuar.upper()  
        if continuar == 'N':
            break
    

    
def excluir():
    catalogo = lercatg()
    placa = int(input('digite a Placa do veículo: '))
    for i in catalogo:
        if i['Placa'] == placa:
            escolha = input('Deseja realmente deletar este veículo de nosso inventario? (S/N) ')
            escolha = escolha.upper()
            if escolha == 'S':
                catalogo.pop()
            salvarcatag(catalogo)
            