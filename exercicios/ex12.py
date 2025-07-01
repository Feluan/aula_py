#lista inicial
lista = [4,5,3,5]
print(lista)


#adiciona um item no final da lista
lista.append(2)
print("apos append (2):" ,lista)


#adiciona um item na posiçao especifica
lista.insert(2, -3)
print("apos insert (2, -3):", lista)

#remove um item especificado da lista
lista.remove(4)
print("apos remove (4):", lista)


#deixa a lista em ordem numerica, ou, alfabetica
lista.sort()
print("apos sort ():", lista)

#inverte a ordem dos elementos
lista.reverse()
print("apos reverse ():", lista)


#conta quantas vezes o valor aparece na lista
quantidade_lista = lista.count(5)
print("quantidade de '5' na lista:" ,quantidade_lista)

#remove e retorna o ultimo item da lista ou de uma posiçao especifica 
item_removido = lista.pop()
print("apos pop ()", lista)
print("item removido com pop():",item_removido)

#remove um item da lista ou de uma posição especifica
del lista[2]
print("apos del lista[2]:",lista)


#limpa a lista
lista.clear()
print("apos clear ():", lista)
