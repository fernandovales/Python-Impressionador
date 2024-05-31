
previsoes = {}
while True:
    nome_produto = str( input('digite o nome do produto(ou "sair" para sair): '))
    if nome_produto.lower() == 'sair':
        break
    vendas_mes_atual = float(input('Digite as vendas do mês atual: '))
    taxa_crescimento = float(input('Digite a taxa de crescimento (%): '))
    #previsao = (taxa_crescimento/100) * vendas_mes_atual + vendas_mes_atual
    previsao = vendas_mes_atual * (1 + taxa_crescimento / 100)
    #previsao = vendas_mes_atual * 1.1 (NÃO PODE USAR ESSA POIS A TAXA VAI VARIANDO)
    previsoes[nome_produto] = previsao

for produto, vendas_proximo_mes in previsoes.items():
    print(f'{produto} , previsão de vendas proximo mes R${vendas_proximo_mes}')
    