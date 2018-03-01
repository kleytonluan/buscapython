class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None
  
class Lista:
    def __init__(self):
        self.inicio=None


    def adicionar(self,item):
        temp = No(item)
        temp.proximo = self.inicio
        self.inicio = temp


    def mostrar(self):

        if self.inicio == None:
              print("Lista vazia")
        else:
              aux = self.inicio
              while aux != None:
                print(aux.valor)
                aux = aux.proximo
                
     def remover(self, item):
        
        atual = self.inicio
        anterior = None
        encontrado = False
        
        while not encontrado:
            if atual.valor == item:
                encontrado = True
            else:
                anterior = atual
                atual = atual.proximo
                
        if anterior == None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo
       
l = Lista()
l.adicionar(1)
l.adicionar(2)
l.adicionar(3)
l.adicionar(4)
l.mostrar()
l.remover(3)
l.mostrar()
