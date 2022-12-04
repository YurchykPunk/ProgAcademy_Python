
class Product:
    def __init__(self, p_title, category, cost = 0, price = 0, stock = 0, discount = 0):
        self.p_title = p_title
        self.category = category
        self.cost = cost
        self.price = price
        self.stock = stock
        self.discount  = discount

    def __str__(self):
        return f'{self.p_title}\t{self.price}\t{self.stock}'

    def procurement(self, q, p):
        self.stock += q
        self.cost += q * p
        return self

    def set_selling_price(self, p):
        self.price = p
        return self
        
    def set_discount(self, d):
        self.price = self.price * (100 - d/100)
        return self
    

product_1 = Product('Cherry Candy', 'candies')
product_2 = Product('Apple candy', 'candies')
product_3 = Product('Chocolate', 'candies')
product_4 = Product('AmericanaCookie', 'cookies')

curr_products = [product_1, product_2, product_3, product_4]

product_1.procurement(21, 12).procurement(21, 12).procurement(37, 10).set_selling_price(15)
product_2.procurement(64, 4).procurement(21, 8).procurement(37, 3).set_selling_price(8)
product_3.procurement(1, 55).procurement(34, 50).procurement(37, 65).set_selling_price(85)

print(product_1, product_1.cost)


class Shopclient:
    def __init__(self, name, surname, age=0, loyalty_card=False, loyalty_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.loyalty_card = loyalty_card
        self.loyalty_id = loyalty_id
        
    def __str__(self):
        return f'Mr(s). {self.surname} {self.name[0]}. - {"registered" if self.loyalty_card else "not registered"}'
    
    def get_loyalty_card(self, a, c_id):
        self.age = a
        self.loyalty_card = True
        self.loyalty_id = c_id
        return self
    
consumer_1 = Shopclient('William', 'Sheakespeare')
consumer_2 = Shopclient('Sherlock', 'Holmes')
consumer_3 = Shopclient('Emmet', 'Brown')
    
curr_consumers = [consumer_1, consumer_2, consumer_3]    

print(consumer_3)
consumer_3.get_loyalty_card(58, 'B213412')
print(consumer_3)

class Order:
    def __init__(self, client):
        self.basket = {}

    def add_to_basket(self, product, quantity):
        self.basket[product.p_title] = quantity
        return self

    def __str__(self):
        checkout_ttl = sum(self.basket.values())
        cl_name = self.client
        return f'{checkout_ttl} {cl_name}'

print(Order(consumer_3).add_to_basket(product_1, 12).add_to_basket(product_3, 12).add_to_basket(product_2, 12))




