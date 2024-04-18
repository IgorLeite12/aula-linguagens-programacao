from datetime import datetime

busca = input("Qual o nome de busca? ")

with open('alunos.csv', 'r') as arquivo:

    next(arquivo)
    lista_linhas = arquivo.readlines()


    for linha in lista_linhas:
        nome, data_de_nascimento, matricula = linha.strip('\n').split(',')
        if nome == busca:
            data_de_nascimento = datetime.strptime(data_de_nascimento, '%d/%m/%Y')
            print(nome, '>', data_de_nascimento)
