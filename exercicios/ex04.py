num1=float(input("Digite um numero a ser calculado: "))
num2=float(input("Digite outro numero a ser calculado: "))
calculo=input("Digite o simbolo referente ao calculo desejado (+, -, x, /)")
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if calculo == "+":
    print(f"Você escolheu soma:\n {num1}+{num2}={soma}")    
elif calculo == "-":
    print(f"Você escolheu subtração:\n {num1}-{num2}={subtracao}")
elif calculo == "x":
    print(f"Você escolheu multiplicação:\n {num1}x{num2}={multiplicacao}")
elif calculo == "/":
    print(f"Você escolheu divisão:\n {num1}/{num2}={divisao}")
else:
    print("nenhuma operação válida foi selecionada.")