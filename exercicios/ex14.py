numeros_reais = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}° número real: "))
    numeros_reais.append(numero)

print("\nOs números na ordem inversa são:")
for numero in reversed(numeros_reais):
    print(numero)
