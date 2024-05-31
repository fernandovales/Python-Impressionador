def analisar_texto(texto):
    
    palavras = texto.split()  # separa com base em espaços
    contagem_palavras = len(palavras)
    frequencia_palavras = {}
    frequencia_letras = {}
    
    for palavra in palavras:
        # abaixo, o get verificará se existe a palavra no dicionário. Não havendo, atribui o valor 0 e soma 1
        frequencia_palavras[palavra] = frequencia_palavras.get(palavra, 0) + 1
        for letra in palavra.lower():
            # abaixo, o get verificará se existe a letra no dicionário. Não havendo, atribui o valor 0 e soma 1
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1
            
    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")