n = int(input("Digite quantas notas q vc quiser: "))
soma = 0

for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / n
print(f"a media aritmetica das {n} notas é: {media: .2f}")

