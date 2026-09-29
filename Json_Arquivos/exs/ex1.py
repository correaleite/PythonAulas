import json

with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    alunos = {}
    for linha in arquivo:
        dados = linha.split(",")
        rm = dados[0]
        nome = dados[1]
        notas = [float(dados[2]), float(dados[3]), float(dados[4]), float(dados[5])]

        alunos[rm] = {"nome": nome, "notas": notas}
    
with open('notasJson.json', 'w', encoding='utf-8') as arquivoJson:
    alunosJson = json.dumps(alunos, indent=4, ensure_ascii=False) 
    arquivoJson.write(alunosJson)