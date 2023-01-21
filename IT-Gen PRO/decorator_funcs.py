#===============================================
#============Task 1 (counter OK)================
#===============================================
#1) Створіть декоратор, який підраховуватиме, скільки разів була
#викликана функція, що декорується.

def counter(victim):
    def inner(*args, **kwargs):
        inner.c += 1
        return victim(*args, **kwargs)
    inner.c = 0
    return inner

@counter
def summer(a, b):
    return a + b

@counter
def suber(a, b):
    return a - b

summer(1,1)
suber(9,1)
suber(2,1)
print(suber.c)


#===============================================
#============Task 2 (reg simple OK)=============
#===============================================
#2) Створіть декоратор, який зареєструє декоровану функцію в
#списку функцій для обробки послідовності.


s = []
def registrator(victim):
    if not victim in s:
        s.append(victim)
    return victim


@registrator
def experimental_a(a, b):
    return a * b

@registrator
def experimental_b(a, b):
    return a ** b

print(experimental_a(2, 5),experimental_b(2, 5), s)


#===============================================
#============Task 3 (txt files add)=============
#===============================================
#3) Припустимо, у класі визначено метод __str__, який повертає
#рядок на основі класу. Створіть такий декоратор для цього методу,
#щоб отриманий рядок зберігався у текстовий файл, ім'я якого
#відповідає імені класу, метод якого ви декорується.


def decorer(victim):
    
    def clsaver(*args):

        with open(f'{args[0].__class__.__name__}.txt', 'a') as savefile:
            res = victim(*args)
            savefile.write(f'{res}\n')
        return res
        
    return clsaver

class Jerry:
        
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @decorer
    def __str__(self):
        return f'Class {self.__class__.__name__} with attributes a={self.a} and b={self.b}'
    

a_1 = Jerry(1,3)
a_2 = Jerry(1,8)
print(a_1)
print(a_2)
print(a_1)



#===============================================
#============Task 4 (eficiency test)============
#===============================================
#4) Створіть декоратор із параметрами для проведення хронометражу роботи
#тієї чи іншої функції. Параметрами повинні виступати те, скільки разів потрібно
#запустити функцію, що декорується, і в який файл зберегти результати
#хронометражу. Мета - провести хронометраж функції, що декорується.


def eficacy_test(repeats, filename):
    import time
    def predator(victim):

        if not isinstance(repeats, int):
            raise TypeError
        elif repeats <= 0:
            raise ValueError

        def translator(*args, **kwargs):

            tac = time.time()
            for _ in range(repeats):
                
                victim(*args, **kwargs)
            tic = time.time()
            with open(str(filename), 'a') as f_save:
                f_save.write(f'{repeats} repeats processed in {tic-tac} seconds\n')
            
            return victim(*args, **kwargs)
        
        return translator
        
    return predator

@eficacy_test(50_000, 't.txt')
def functest(a, b):
    return a ** b
