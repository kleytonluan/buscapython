import time
import random
def buscasequencialrecursiva(vetor, valor, tamanho):
        if tamanho == 1: #Se tamanho for igual a 1
                if vetor[0] == valor: #Se o elemento [0] do vetor foi igual ao valor
                        return 0 #Retorna [0] Verdadeiro
                else: #Se nao
                        return -1 #Retorna [-1] falso
        else: #Se nao
                i = buscasequencialrecursiva(vetor, valor, tamanho -1) #Indice chama o metodo novamente
                if i < 0: #Se indice for menor que 0
                        if vetor[tamanho -1] == valor: #Se o tamanho do vetor - 1 foi igual a o valor
                                i = tamanho-1 #Indice recebe o tamanho - 1
                return i #Retorna indice dentro do if i < 0:
antes = time.time()
vetor = (range(500))
random.shuffle(vetor)
print(vetor)
print buscasequencialrecursiva(vetor, 5, len(vetor))
depois = time.time()
total = (depois-antes)*1000

print("Tempo de execucao: %0.2f ms" % total)
