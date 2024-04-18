# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

def soma(valor1, valor2):
    soma = valor1 + valor2

def subtracao(valor1, valor2):
    subtracao = valor1 - valor2

def multiplicacao(valor1, valor2):
    multiplicacao = valor1 * valor2

def divisao(valor1, valor2):
    divisao = valor1 / valor2

valor1 = int(input("N1: "))
operador = input("1.soma\n2.subtração\n3.multiplicação\n4.divisão")
valor2 = int(input("N2: "))



if operador == "1":
    soma()
    print("Resultado:",soma())

elif operador == "-":
    resultado = valor1 - valor2
    print("Resultado:",resultado)
    
elif operador == "*":
    resultado = valor1 * valor2
    print("Resultado:",resultado)

elif operador == "/":
    resultado = valor1 / valor2
    print("Resultado:",resultado)