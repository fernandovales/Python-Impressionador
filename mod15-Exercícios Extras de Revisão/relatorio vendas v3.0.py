def solicitar_nome_vendedor():
    return input('digite o nome do vendedor(ou "sair" para sair): ')


def solicitar_vendas():
    try:
        return float(input ('digite as vendas: '))
    except ValueError:
        print('entrada inválida. digite um numero para vendas.')
        return None


def atualizar_dados (dados_vendas,nome,vendas):
    if nome not in dados_vendas:
        dados_vendas[nome]={'total':vendas,'qtde':1}
    else:
        dados_vendas[nome]['total'] += vendas
        dados_vendas[nome]['qtde'] += 1
        
        
def printar_dados(dados_vendas):
    for nome,dados in dados_vendas.items():
        total = dados['total']
        media = total / dados['qtde']
        print(f'{nome}: total de vendas = R${total:.2f}, média de vendas =R${media:.2f}')
        
    
def main():
    dados_vendas = {}
    while True:
        nome = solicitar_nome_vendedor()
        if nome.lower() =='sair':
            break
        vendas = solicitar_vendas()
        if vendas is None:
            continue
        atualizar_dados(dados_vendas,nome,vendas)
    printar_dados(dados_vendas)
    
if __name__== "__main__":
    main()

