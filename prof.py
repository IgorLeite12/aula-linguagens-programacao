from datetime import datetime

with open('eu.txt', 'w') as arquivo:
    arquivo.write('igor Matheus Viana Leite\n')
    hoje = str(datetime.now().strftime('%d/%m/%Y'))
    arquivo.write(hoje)
    arquivo.write('\t')
    arquivo.write('Manuas - AM\n')
    arquivo.write('18')
    arquivo.write('\t')
    arquivo.write('Sao Lazaro\n')

    disciplina = input('nome da disciplina: ')
    while disciplina != 'sair':
        dis = disciplina
        arquivo.write(dis + ', ')

        nota = input('nota: ')
        notr = nota
        arquivo.write(notr + '\n')
        disciplina = input('nome da disciplina: ')
        

    