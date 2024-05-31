dados_vendas = dict()

while True:
    nome = input('digite o nome do vendedor(ou "sair" para sair): ')
    if nome.lower() == 'sair':
        break
    vendas = float(input('digite as vendas: '))
    if nome not in dados_vendas:
        dados_vendas[nome] = [vendas]
    else:
        dados_vendas[nome].append(vendas)
    
print(dados_vendas)
for nome,vendas in dados_vendas.items():
    total = sum(vendas)
    media = total / len(vendas)
    print(f'{nome}, total de vendas: R${total}, media de vendas R${media}')