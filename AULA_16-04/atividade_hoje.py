from datetime import datetime

with open('atividade_hoje.txt', 'a') as arquivo:
    nome = 'igor matheus viana leite'
    texto = nome.upper + '\n'
    arquivo.write(texto)