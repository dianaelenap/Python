class Product:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
    
    def __str__(self):
        return "Produsul %s este in cantitate de %d" % (self.name,self.quantity)

    def diff(self,produs):
        if(self.quantity > produs.quantity):
            diff = self.quantity - produs.quantity
        elif(self.quantity <= produs.quantity):
            diff = produs.quantity - self.quantity
        return diff
