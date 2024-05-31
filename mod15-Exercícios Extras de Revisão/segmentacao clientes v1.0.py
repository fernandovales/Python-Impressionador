clientes = {}
while True:
    nome = input('digite o nome do cliente ou 999 para sair: ')
    if nome == '999':
        break
    compras = float(input('digite o total das compras: '))
    if compras <= 1000:
        segmento = 'bronze'
    elif compras <= 5000:
        segmento = 'prata'
    else:
        segmento = 'ouro'
    clientes[nome] = segmento
    
print(clientes)
for nome,segmento in clientes.items():
    print(f'{nome}, segmento: {segmento}')