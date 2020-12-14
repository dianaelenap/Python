class Product:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
    
    def __str__(self):
        return "Produsul %s este in cantitate de %d" % (self.name,self.quantity)

