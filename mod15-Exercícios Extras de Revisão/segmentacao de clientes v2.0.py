clientes = {}
segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
while True:
    nome = input('digite o nome do cliente ou 999 para sair: ')
    if nome == '999':
        break
    while True:
        try:
            compras = float(input('digite o total das compras: '))
            if compras < 0:
                print('erro. difgite um valor de comparas que seja positivo.')
                continue
            break
        except ValueError:
            print('erro. por favor digite um valor valido.')
    
    for limite,segmento in segmentos:
        if compras <= limite:
            clientes[nome] = segmento
            break
    
print(clientes)
for nome,segmento in clientes.items():
    print(f'{nome}, segmento: {segmento}')