import time
import random
def busca_sequencial_sentinela(v, x):
    i = 0
    v.append(x)#Adicionar no final do vetor
    while v[i] != x:
        i += 1

    if i == len(v)-1:
        return -1
    return i

antes = time.time()
vetor = list(range(1000000))
random.shuffle(vetor)
#print(lista)
chave = 9999
posicao = busca_sequencial_sentinela(vetor, chave)
depois = time.time()
total = (depois-antes)*1000
if posicao >= 0:
    print("Busca da chave %d encontrada na posicao %d " % (chave, posicao))
else:
    print("Nada foi encontrado")
print("Tempo de execucao: %0.2f ms" % total)
