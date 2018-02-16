import random
import time
#_______busca sequencial com sentinela

def busca_sentinela(vetor, valor):
    i = 0
    vetor.append(valor)
    while vetor[i] != valor:
        i += 1

    if i == len(vetor)-1:
        return -1
    return i

antes = time.time()
lista = list(range(10))
valor = int(input("Digite uma busca com sentinela: "))
print(busca_sentinela(lista,valor))
depois = time.time()
total = (depois-antes)*1000
print("Executado em: %0.2f ms" % total)

#_______busca sequencial

def busca(vetor,valor):
    i = 0
    while i < len(vetor):
        if vetor[i] == valor:
            return i
        i += 1
    return -1

antes = time.time()
valor = int(input("Digite uma busca normal: "))
print(busca(lista,valor))
depois = time.time()
total = (depois-antes)*1000
print("Executado em: %0.2f ms" % total)

#_______Busca com recursividade

def busca_recursiva(vetor, valor, tamanho):
    if tamanho == 1:
        if vetor[0] == valor:
            return 0
        else:
            return -1
    else:
        i = busca_recursiva(vetor,valor,tamanho -1)
        if i < 0:
            if vetor[tamanho-1] == valor:
                i = tamanho-1
        return i

antes = time.time()
valor = int(input("Digite uma busca com recursividade: "))
print (busca_recursiva(lista,valor,len(lista)))
depois = time.time()
total = (depois-antes)*1000
print("Executado em: %0.2f ms" % total)

#_______recursividade

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1 )
    
antes = time.time()
valor = int(input("Digite um numero para calcular seu fatorial: "))
resultado = fatorial(valor)
print(fatorial(valor))
depois = time.time()
total = (depois-antes)*1000
print("Executado em: %0.2f ms" % total)


