def buscaRecursiva(vetor,valor,tamanho):
	if tamanho == 1:
		if vetor[0] == valor:
			return 0
		else:
			return -1
	else:
		i = buscaRecursiva(vetor,valor,tamanho-1)
		if i > 0:
			if vetor[tamanho -1] == valor:
				i = tamanho -1
		return i
	
lista = list(range(10))
busca = int(input("Digite a busca:"))
print buscaRecursiva(lista,busca,len(lista))
  
