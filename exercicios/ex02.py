num1= int(input("Digite um numero "))
num2= int(input("Digite outro numero "))
if num1 > num2:
    print(f"o numero maior é {num1}")
    print(f"o numero menor é {num2}")
elif num2 > num1:
    print(f"o numero maior é {num2}")
    print(f"o numero menor é {num1}")
else:
    print("os dois numeros sao iguais")
   