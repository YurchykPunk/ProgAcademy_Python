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