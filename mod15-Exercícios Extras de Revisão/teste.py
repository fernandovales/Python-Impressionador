# solução


def solicitar_nome_cliente():
    return input("Digite o nome do cliente (ou 'sair' para sair): ").lower()


def solicitar_total_compras():
    try:
        return float(input("Digite o total de compras: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        return None
    

def atribuir_segmento(compras, segmentos):
    for limite, segmento in segmentos:
        if compras <= limite:
            return segmento
        

def print_segmento_por_cliente(clientes):
    for nome, segmento in clientes.items():
        print(f"{nome}: Segmento do Cliente = {segmento}")
        

def main():
    segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
    clientes = {}
    while True:
        nome = solicitar_nome_cliente()
        if nome == 'sair':
            break
        compras = solicitar_total_compras()
        if compras is None:
            continue
        clientes[nome] = atribuir_segmento(compras, segmentos)
    print_segmento_por_cliente(clientes)

    
if __name__ == "__main__":
    main()
    