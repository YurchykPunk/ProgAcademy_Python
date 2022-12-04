
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


product_1.procurement(21, 12).procurement(21, 12).procurement(37, 10).set_selling_price(15)
product_2.procurement(64, 4).procurement(21, 8).procurement(37, 3).set_selling_price(8)
product_3.procurement(1, 55).procurement(34, 50).procurement(37, 65).set_selling_price(85)


class Shopclient:
    def __init__(self, name, surname, age=0, loyalty_card=False, loyalty_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.loyalty_card = loyalty_card
        self.loyalty_id = loyalty_id
        
    def __str__(self):
        return f'Mr(s). {self.surname} {self.name[0]}.'
    
    def get_loyalty_card(self, a, c_id):
        self.age = a
        self.loyalty_card = True
        self.loyalty_id = c_id
        return self
    
consumer_1 = Shopclient('William', 'Sheakespeare')
consumer_2 = Shopclient('Sherlock', 'Holmes')
consumer_3 = Shopclient('Emmet', 'Brown')
    

consumer_3.get_loyalty_card(58, 'B213412')

class Order:
    def __init__(self, client):
        self.client = client
        self.basket = {}

    def add_to_basket(self, product, quantity=1):
        self.basket[product] = quantity
        return self

    def checkout_sum(self):
        t_amount = sum(x.price * self.basket[x] for x in self.basket)
        return t_amount

    def __str__(self):
        qties_basket = self.basket.values()
        cheque_header = f'{"-"*35}\n{self.client}\n{"-"*35}\n'
        cheque = cheque_header + ''.join(map(
            lambda z: f'{z[0]} x {z[1]}\t= \t{z[0].price * z[1]}\n',\
            zip(self.basket, qties_basket)))

        return f'{cheque}\n{"-"*35}\nTotal: \t{self.checkout_sum()}\n{"-"*35}'




order_1 = Order(consumer_3)
order_1.add_to_basket(product_1, 1).add_to_basket(product_3, 2).add_to_basket(product_2, 15)
print(order_1)




