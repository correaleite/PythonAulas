arquivo = open('ips.txt', 'r')
arquivoConjunto = set(arquivo)

with open('ipsNovo.txt', 'w', encoding='utf-8') as arquivoNovo:
    for item in arquivoConjunto:
        arquivoNovo.write(item + '\n')

arquivo.close()
arquivoNovo.close()