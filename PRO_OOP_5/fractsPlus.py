#2. Створіть клас «Правильна дроба» та реалізуйте методи
#порівняння, додавання, віднімання та множення для екземплярів цього класу.
#creating new instance option

class Trulyfraction:
    def __init__(self, numerator, denominator=1):
        if abs(denominator) < abs(numerator):
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator
        if self.numerator * self.denominator < 0:
            self.numerator = -abs(self.numerator)
            self.denominator = abs(self.denominator)
        self.hcf_calculator()

    def hcf_calculator(self):
        common_factor = 1
        flag = 1
        num_hcf, den_hcf = abs(self.numerator), self.denominator
        
        while flag:
            head = den_hcf%num_hcf
            common_factor = num_hcf
            den_hcf = num_hcf
            num_hcf = head
            flag = num_hcf
            
        self.numerator //= common_factor
        self.denominator //= common_factor
        return self
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
                
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator
        
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator
        
    def __lq__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Trulyfraction(new_numerator, new_denominator).hcf_calculator()
        
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Trulyfraction(new_numerator, new_denominator).hcf_calculator()

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Trulyfraction(new_numerator, new_denominator).hcf_calculator()


af = Trulyfraction(17,42)
bf = Trulyfraction(9,42)
cf = Trulyfraction(20, 40)

print(af==bf)
print(af+bf)
print(af-bf)
print(af*bf)
print(cf)
