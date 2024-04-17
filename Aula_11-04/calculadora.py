# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1

valor1 = int(input("N1: "))
valor2 = int(input("N2: "))
operador = input(" '+' '-' '*'  '/' ")

while resultado != '-1':
        nn = int(input("Digite um número: "))
        operador = input(" '+' '-' '*'  '/' ")
        resultado = resultado + nn
        print(resultado)


if operador == "+":
    resultado = valor1 + valor2
    print("Resultado:",resultado)

elif operador == "-":
    resultado = valor1 - valor2
    print("Resultado:",resultado)
    
elif operador == "*":
    resultado = valor1 * valor2
    print("Resultado:",resultado)

elif operador == "/":
    resultado = valor1 / valor2
    print("Resultado:",resultado)

    