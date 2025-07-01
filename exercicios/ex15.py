notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("\nAs notas são:", notas)
print(f"A média das notas é: {media:.2f}")
