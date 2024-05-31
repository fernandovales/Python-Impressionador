def solicitar_nome():
    return input('digite o nome do cliente ou 999 para sair: ')

def solicitar_compras():
    try:
        return float(input('digite o total das compras: '))
    except ValueError:
        print('erro. por favor digite um valor valido.')
        return None
    
def verificar_segmento(compras,segmentos):
     for limite,segmento in segmentos:
        if compras <= limite:
            return segmento
            
            
def print_segmentar_clientes(clientes):
    for nome,segmento in clientes.items():
        print(f'{nome}, segmento: {segmento}')
        
    
    
def main():
    clientes = {}
    segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
    while True:
        nome = solicitar_nome()
        if nome == '999':
            break
        compra = solicitar_compras()
        if compra is None:
            continue
        clientes[nome] = verificar_segmento(compra,segmentos)
    print_segmentar_clientes(clientes)
    
    
if __name__ == "__main__" :
    main()

    
        