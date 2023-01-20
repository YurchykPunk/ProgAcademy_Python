#1) Створіть декоратор, який зареєструє клас, що декорується в
#списку класів.

#2) Створіть клас декоратора з параметром. Параметром має бути
#рядок, який повинен дописуватися (ліворуч) до результату роботи методу __str__.

#3) Для класу Box напишіть статичний метод, який буде підраховувати
#сумарний обсяг двох ящиків, які будуть його параметрами.

#======================TASK 1=========================

classes = []

def registrator(cls):    
    classes.append(cls)
    return cls

@registrator
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
print(classes, A(2,4))


#======================TASK 2=========================

classes = []

class B:
    def __init__(self, arg):
        self.arg = arg
        
    def __call__(self, cls):
        
        old_text = cls.__str__                          #-0- assign func to var
        
        def __str__(self):                              #-2- new function - str substit
            return f'{self.temp_str}{old_text(self)}'
        
        cls.temp_str = self.arg                         #-1- creates var in Class
        cls.__str__ = __str__                           #-3- reassigns str function
        
        return cls


    
@B('Text I forgot to add initially. ')
class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'Here we are {self.a} {self.b}'
    
    
bb = C(1,3)
print(bb)
bb.a = 21321
print(bb)


#======================TASK 3=========================

class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.volume = self.a * self.b * self.c
    
    @staticmethod
    def volume_sum(*args):
        return sum([x.volume for x in args])



aa = Box(1,2,4)
bb = Box(4,5,6)
cc = Box(20, 50, 2)

print(aa.volume)
print(bb.volume)
print(cc.volume)
print(Box.volume_sum(aa, bb, cc))
