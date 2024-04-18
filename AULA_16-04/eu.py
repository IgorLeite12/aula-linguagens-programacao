from datetime import datetime

with open('eu.txt', 'w') as arquivo:
    arquivo.write('Igor Matheus Viana Leite\n')
    hoje = datetime.now().strftime('%d/%m/%Y')
    arquivo.write(hoje)
    arquivo.write('\t')
    arquivo.write('Manaus - AM\n')
    arquivo.write('18')
    arquivo.write('\t')
    arquivo.write('São Lázaro\n')

    disciplina = input('Digite a disciplina ou "sair" para encerrar: ')
    while disciplina != 'sair':
        nota = input('Digite a nota correspondente: ')
        arquivo.write(disciplina + ', ' + nota + '\n')
        disciplina = input('Digite a próxima disciplina ou "sair" para encerrar: ')
