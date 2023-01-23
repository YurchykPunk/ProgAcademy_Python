import abc

class PrimeBlank(abc.ABC):
    
    @abc.abstractmethod
    def prime_check(n):
        ...
    
class MyClass(PrimeBlank):
    
    def __init__(self, a):
        self.a = a

    def prime_check(self):
        if self.a <= 1:
            return False
        for x in range(2, self.a // 2 + 1):
            if not self.a%x:
                return False
        else:
            return True        
    
class CloneClass:
    
    def __init__(self, a):
        self.a = a

    def completely_not_prime_check(self):
        if self.a <= 1:
            return False
        for x in range(2, self.a // 2 + 1):
            if not self.a%x:
                return False
        else:
            return True        
    

PrimeBlank.register(CloneClass)

x = MyClass(19)
y = CloneClass(23)
print(isinstance(x, PrimeBlank))
print(isinstance(y, PrimeBlank))
