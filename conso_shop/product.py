import excepts

class Product:
    def __init__(self, p_title, category, cost = 0, price = 0, stock = 0, discount = 0):
        self.p_title = p_title
        self.category = category
        self.cost = cost
        self.price = price
        self.stock = stock
        self.discount  = discount

    def __str__(self):
        return f'{self.p_title}\t{self.price}'

    def procurement(self, q, p):
        if not isinstance(q, (float, int)) or not isinstance(p, (float, int)):
            raise ValueError()
                
        if q <= 0:
            raise excepts.StockError(q)
        if p <= 0:
            raise excepts.PriceError(p)
                
        self.stock += q
        self.cost += q * p
        return self

    def set_selling_price(self, p):
        if not isinstance(p, (float, int)):
            raise ValueError()
                
        if p <= 0:
            raise excepts.PriceError(p)
                
        self.price = p
        return self
        
    def set_discount(self, d):
        self.price = self.price * (100 - d/100)
        return self