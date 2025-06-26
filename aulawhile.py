notas = 0 
qnt_notas_info = 0
while True: 
    nota = float(input("digite -1 para sair, ou a nota para continuar "))
    if nota == -1:
        break
    notas = nota + nota
    qnt_notas_info = qnt_notas_info + 1
    if qnt_notas_info > 0 :
        media = notas/qnt_notas_info
        print(f"Quantidade de notas informadas {qnt_notas_info}")
        print(f"Média {media}")
    else:
        print("Nenhuma nota informada")