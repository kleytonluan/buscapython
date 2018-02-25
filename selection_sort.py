import random

def selection_sort(vetor):
	i = 0
	while i < len(vetor)-1:
		menor = i
		j = i + 1
		
		while j < len(vetor):
			if vetor[j] < vetor[menor]:
				menor = j
			j += 1
			
		if menor != i:
			temp = vetor[i]
			vetor[i] = vetor[menor]
			vetor[menor] = temp
		i += 1
			
				
vetor = list(range(10))
random.shuffle(vetor)
print("Vetor desordenado",vetor)
selection_sort(vetor)
print("Vetor ordenado",vetor)
