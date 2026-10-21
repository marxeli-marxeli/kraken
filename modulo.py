p1 = {"nome": "Mouse", "preco": 45.9, "estoque":12}
p2 = {"nome": "Cabo", "preco": 25.0, "estoque": 2}


class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
 
    def vender(self, qtd):
        if qtd > self.estoque:
            return False
        self.estoque -= qtd
        return True
 
    def mostrar(self):
        print(self.nome, self.estoque)
       
mouse = Produto("Mouse", 45.9, 12)
print(mouse.vender(5)) 
mouse.mostrar()  
print(mouse.vender(50))

