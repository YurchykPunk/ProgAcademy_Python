#1. Реалізуйте генераторну функцію, яка повертатиме по одному 
#члену геометричної прогресії із зазначеним множником.
#Генератор повинен зупинити свою роботу або після досягнення 
#зазначеного елементу, або при передачі команди на завершення.

#2. Реалізуйте свій аналог генераторної функції range().

#3. Напишіть функцію-генератор, яка повертатиме прості числа. 
#Верхня межа діапазону повинна бути задана параметром цієї функції.

#4. Напишіть генераторний вираз для заповнення списку. Список повинен 
#бути заповнений кубами чисел від 2 до вказаної вами величини.

#=========Excercise_1=================

def geo_gener(start, peak, multi = 2):
    counter = 1
    while counter <= peak:
        yield start
        start *= multi
        counter += 1

#=========Excercise_2=================

def par_ranger(*args):
    s, f, step = 0, None, 1
    if len(args) == 1:
        f = args
    elif len(args) == 2:
        s, f = args
    elif len(args) == 3:
        s, f, step = args
    
    if not step:
        raise ValueError
    
    if step > 0 and f < s:
        return
    if step < 0 and f > s:
        return    
    
    while abs(s) < abs(f):
        yield s
        s += step
    

#=========Excercise_3 -- OK -- =================

def prime_gener_b(peak):
    for y in range(2, peak + 1):
        for x in range(2, y // 2 + 1):
            if not y%x:
                break
        else:
            yield y
            

#=========Excercise_4 -- OK -- =================

g = (x**3 for x in range(2,15))
print(*g)

#for x in geo_gener(6, 3):
#    print(x)
    
bb = prime_gener_b(190)
for x in bb:
    if x > 55:
        bb.close()
    print(x)
