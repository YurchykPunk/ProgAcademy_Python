#Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння
#прямокутників за площею. Також реалізуйте методи складання прямокутників (площа сумарного
#прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте). Реалізуйте методи
#множення прямокутника на число n (це має збільшити площу базового прямокутника у n разів).

class UnrealRectangleErr(Exception):
    def __init__(self, r_1, r_2):
        self.r_1 = r_1
        self.r_2 = r_2
    def __str__(self):
        return f'Error: you can`t create one rectangle by adding {self.r_1} and {self.r_2}'\
            ' since they must have at least one similar side'




class Rectangle:
    def __init__(self, width, lenght):
        if not isinstance(width, (int, float)) or not isinstance(lenght, (int, float)):
            raise TypeError('Definitely the dimensions should be comprised from numbers!')        
        
        self.width = width
        self.lenght = lenght
        self.area = self.width * self.lenght
        
    def reset_area(self):
        self.area = self.width * self.lenght
        return self.area

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

#to me, multiplying area is total mess!
    def __mul__(self, other):
        self.lenght = self.lenght * other
        self.reset_area()
        return self
    
    def __add__(self, other):
        rec_set_1 = set([self.width, self.lenght])
        rec_set_2 = set([other.width, other.lenght])
        check = rec_set_1&rec_set_2
        if rec_set_1&rec_set_2:
            dim_1 = min(check)
            dim_2a = list(rec_set_1-{dim_1})[0] if len(rec_set_1)==2 else list(rec_set_1)[0]
            dim_2b = list(rec_set_2-{dim_1})[0] if len(rec_set_2)==2 else list(rec_set_2)[0]
            dim_2 = dim_2a + dim_2b
            return Rectangle(min(dim_1, dim_2),max(dim_1, dim_2))
        else:
            raise UnrealRectangleErr(self, other)


    def __str__(self):
        return f'rectangle with sides {self.width}x{self.lenght}'


rec_1 = Rectangle(8,3)
rec_2 = Rectangle(9,30)
print(rec_1.area)
rec_1 = rec_1*10
print(rec_1.area)
try:
    rec_3 = rec_1+rec_2
    print(rec_3, rec_3.area, sep="\t")
except Exception as err:
    print(err)
print(rec_1, rec_1.area, sep="\t")
print(rec_2, rec_2.area, sep="\t")
