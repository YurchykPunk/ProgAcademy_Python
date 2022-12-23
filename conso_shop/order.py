import order_itera

class Order:

    def __init__(self, client):
        self.client = client
        self.basket_products = []
        self.basket_qties = []

    def add_to_basket(self, product, quantity=1):
        if product in self.basket_products:
            self.basket_qties[self.basket_products.index(product)] += quantity
        else:
            self.basket_products.append(product)
            self.basket_qties.append(quantity)
        return self

    def checkout_sum(self):
        t_amount = sum(x.price * self.basket_qties[index] for index, x in enumerate(self.basket_products))
        return t_amount

    def __len__(self):
        return len(self.basket_products)
    
    def __getitem__(self, index):
        if not isinstance(index, (slice, int)):
            raise TypeError
        elif isinstance(index, int) and index < len(self.basket_products):
            return self.basket_products[index]
        elif isinstance(index, slice):
            start = index.start or 0
            stop = index.stop or len(self.basket_products)-1
            step = index.step or 1
            result = []
            for x in range(start, stop, step):
                result.append(self.basket_products[x])
            return result
        raise IndexError

    def __iter__(self):
        return order_itera.OrderIterator([self.basket_products, self.basket_qties])


    def __str__(self):
        cheque_header = f'{"*"*35}\n{self.client}\n{"-"*35}\n'
        cheque = cheque_header + ''.join(map(
            lambda z: f'{z[0]} x {z[1]}\t= \t{z[0].price * z[1]}\n',\
            zip(self.basket_products, self.basket_qties)))

        return f'{cheque}\n{"-"*35}\nTotal:\t\t{self.checkout_sum():.2f} UAH\nVAT included:\t{self.checkout_sum()/6:.2f} UAH\n{"-"*35}'
