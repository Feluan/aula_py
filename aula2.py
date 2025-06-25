n1 = float(input())
n2 = float(input())
media = (n1+n2)/2
if media >= 7:
    print(f"Sua média final é {media:.2f}, e você foi aprovado!!")
elif media > 4:
    print(f"Sua média final é {media:.2f}, e você esta de recuperação.")
else:
    print(f"Sua média final é {media:.2f}, e você foi reprovado.")
    