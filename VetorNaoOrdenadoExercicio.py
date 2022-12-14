class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0]

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self,valor):
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade maxima atingida")
        else:            
            for i in range(self.ultima_posicao + 1):
                if valor == self.valores[i]:
                    return 
            self.ultima_posicao = self.ultima_posicao + 1
            self.valores[self.ultima_posicao] = valor
            
        
    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1
            
vetor = VetorNaoOrdenado(8)
vetor.imprime()
print()

vetor.insere(4)
vetor.insere(2)
vetor.insere(2)
vetor.insere(5)
vetor.insere(6)
vetor.insere(7)
vetor.insere(4)
vetor.insere(1)
vetor.insere(2)
vetor.insere(3)
vetor.insere(8)
vetor.insere(9)
vetor.imprime()
