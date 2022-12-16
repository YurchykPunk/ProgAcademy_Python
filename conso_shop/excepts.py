class PriceError(Exception):
    def __init__(self, subj):
        self.subj = subj
    
    def __str__(self):
        return f'Entered price -- {self.subj} -- is totally invalid value'

class StockError(Exception):
    def __init__(self, subj):
        self.subj = subj
    
    def __str__(self):
        return f'Entered stock -- {self.subj} -- is totally invalid value'