valor1 = int(input("N1: "))
valor2 = int(input("N2: "))
operador = input(" '+' '-' '*'  '/' ")

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
