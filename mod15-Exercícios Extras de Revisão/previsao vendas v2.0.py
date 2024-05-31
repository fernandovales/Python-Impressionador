previsoes = {}

while True:
    nome_produto = input('Digite o nome do produto (ou "sair" para sair): ')
    if nome_produto.lower() == 'sair':
        break
    
    # Validação das vendas do mês atual
    while True:
        try:
            vendas_mes_atual = float(input('Digite as vendas do mês atual: '))
            if vendas_mes_atual < 0:
                print("Erro. Por favor, insira um valor positivo.")
                continue
            break
        except ValueError:
            print("Erro. Por favor, insira um valor numérico válido.")
    
    # Validação da taxa de crescimento
    while True:
        try:
            taxa_crescimento = float(input('Digite a taxa de crescimento (%): '))
            if taxa_crescimento < 0:
                print("Erro. Por favor, insira um valor positivo.")
                continue
            break
        except ValueError:
            print("Erro. Por favor, insira um valor numérico válido.")
    
    previsao = vendas_mes_atual * (1 + taxa_crescimento / 100)
    previsoes[nome_produto] = previsao

print(previsoes)
for produto, vendas_proximo_mes in previsoes.items():
    print(f'{produto}, previsão de vendas próximo mês R${vendas_proximo_mes}')
