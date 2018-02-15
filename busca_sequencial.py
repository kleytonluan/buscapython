import time
def BuscaSequencial(v, x):
        i = 0
        while i < len(v):
                if v[i] == x:
                        return i
                i += 1
        return -1

antes = time.time()
vetor = (range(1000000))
#print(vetor)
print BuscaSequencial(vetor, 9999)
depois = time.time()
total = (depois-antes)*1000

print("Tempo de execucao: %0.2f ms" % total)
