
#1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової
#послідовності, закон якої задається за допомогою функції користувача.
# Крім цього параметром генераторної функції повинні бути значення першого члена
#прогресії та кількість членів, що видаються послідовностю.
# Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при 
#передачі команди на завершення.
#2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація.
#Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення
#n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.
#3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне
#суми елементів отриманого списку.


#=============== Task 1 ===============

def progression_geo(a):
    return a * 3

def progression_arith(a):
    return a + 3

def genertest(start, peak, funcey):
    index = start
    while index <= peak:
        worker = funcey(start)
        yield worker
        start = worker
        index += 1



#for x in genertest(1, 10, progression_geo):
#    print(x)

#=============== Task recurs =========

def fibie_slow(n):
    if n <= 1:
        return n
    
    return fibie_slow(n-1) + fibie_slow(n-2)
    

#=============== Task 2 ===============

def memorise():
    memo = [0, 1]
    def fibbi(element):
        if element + 1 <= len(memo):
            return memo[element]
        while len(memo) <= element:
            memo.append(sum(memo[-2:]))            
        return memo[element]
    return fibbi

zz = memorise()
print(zz(1))
print(zz(7))

#=============== Task 3 ===============

def fun_summer(u, funcey):
    nums_to_sum = []
    for x in u:
        nums_to_sum.append(funcey(x))
        print(funcey(x))
    return sum(nums_to_sum)

print(fun_summer([1,2,3,4,5], progression_geo), '-  -')
print(fun_summer([1,2,3,4,5], lambda x: x ** 2 - x), '-  -')
