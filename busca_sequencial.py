def BuscaSequencial(v, x):
        i = 0
        while i < len(v):
                if v[i] == x:
                        return i
                i += 1
        return -1

vetor = (range(100))
print BuscaSequencial(vetor, 9999)
