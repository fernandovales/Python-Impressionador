dados_vendas = dict()


while True:
    while True:
        try:
            nome = input('digite o nome do vendedor(ou "sair" para sair): ')
            if len(nome) <= 3:
                print('erro. nome precisa ter mais de 3 caaracteres.')
                continue
            break
        except ValueError:
            print('erro. nome precisa ter mais 3 caracteres.')
            
    if nome.lower() == 'sair':
        break
    while True:
        try:
            vendas = float(input('digite as vendas: '))
            if vendas < 0:
                print('Erro ao informar valor de vendas.')
                continue
            break
        except ValueError:
            print('Erro ao informar valor de vendas.')
        
    if nome not in dados_vendas:
        dados_vendas[nome] = {'total':vendas,'qtde': 1}
    else:
        dados_vendas[nome]['total'] += vendas
        dados_vendas[nome]['qtde'] += 1
        
print(dados_vendas)

for nome, vendas in dados_vendas.items():
    total = vendas['total']
    media = total / vendas['qtde']
    print(f'{nome}, total de vendas R${total}, média de vendas R${media}')
