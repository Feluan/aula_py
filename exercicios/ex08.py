nota = float(input("Digite uma nota entre 0 e 10: "))

while True:
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Erro: A nota deve estar entre 0 e 10.") 

            