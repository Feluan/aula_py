soma = 0 

while True:
    numero = int(input("Digite um numero (digite 0 para encerrar): "))
    if numero == 0: 
        break
    soma += numero
print(f"A soma de todos os numeros digitados é: {soma}")


