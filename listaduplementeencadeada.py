#lista duplamente encadeada
class No(object):
	def __init__(self, dado, anterior, proximo):
		self.dado = dado
		self.proximo = proximo
		self.anterior = anterior
class ListaDuplementeEncadeada(object):
	
	inicio=None
	fim=None
	
	def adicionar(self, dado):
		novo_no= No(dado, None, None)
		if self.inicio is None:
			self.inicio = novo_no
			self.fim = novo_no
		else:
			novo_no.anterior = self.fim
			novo_no.proximo = None
			self.fim.proximo = novo_no
			self.fim = novo_no
			
	def remover(self,dado):
		no_atual = self.inicio
		
		while no_atual is not None:
			if no_atual.dado == dado:
				if no_atual.anterior == None:
					self.inicio = no_atual.proximo
					no_atual.proximo.anterior = None
				else:
					no_atual.anterior.proximo = no_atual.proximo
					no_atual.proximo.anterior = no_atual.anterior
			no_atual = no_atual.proximo
	
	def imprimir(self):
		print ("Lista Duplamente Encadeada")
		
		no_atual = self.inicio
		no = ""
		
		while no_atual is not None:
			if no_atual.anterior is None:
				no += "None "
			no += "<--> | " + str(no_atual.dado) + " | "
			if no_atual.proximo is None:
				no += "<---> None"
				
			no_atual = no_atual.proximo
		print no
		print "="*60

lista = ListaDuplementeEncadeada()
lista.adicionar(10)
lista.imprimir()
lista.adicionar(12)
lista.imprimir()
lista.adicionar(16)
lista.imprimir()
lista.adicionar(19)
lista.remover(10)
lista.imprimir()

