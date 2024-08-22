def obter_sabor():
    sabores = {
        '1': 'Calabresa',
        '2': 'Frango com Catupiry',
        '3': 'Moda da Casa',
        '4': 'Atum'
    }
    while True:
        nome = input('Digite o sabor da pizza'
                     '\nCalabresa = 1'
                     '\nFrango com Catupiry = 2'
                     '\nModa da Casa = 3'
                     '\nAtum = 4\n')
        if nome in sabores:
            return nome
        print('Sabor inválido. Por favor, escolha um número de 1 a 4.')

def obter_adicionais():
    adicionais = []
    adicionais_opcoes = {
        '1': 'Cheddar $6',
        '2': 'Bacon $6'
    }
    while True:
        adicional = input('Escolha os adicionais ou pressione Enter para continuar'
                          '\nCheddar $6 = 1'
                          '\nBacon $6 = 2\n')
        if adicional == '':
            break
        if adicional in adicionais_opcoes:
            adicionais.append(adicional)
        else:
            print('Adicional inválido. Escolha 1 ou 2 para adicionar um adicional.')
    return adicionais

def obter_tamanho():
    tamanhos = {'P': 'Pequena', 'M': 'Média', 'G': 'Grande'}
    while True:
        tamanho = input('Informe o tamanho da pizza (P, M, G): ').upper()
        if tamanho in tamanhos:
            return tamanho
        print('Tamanho inválido. Escolha P, M ou G.')