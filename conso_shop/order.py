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