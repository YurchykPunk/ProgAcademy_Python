#===============================================================
#====================TASK 1=====================================
#===============================================================

class Manager:

    def __init__(self, naming):
        self.naming = naming
        
    def __set__(self, instance_self, value):
        if self.naming not in instance_self.__dict__:
            instance_self.__dict__[self.naming] = value
        else:
            raise AttributeError('read-only attribute')
        
    def __get__(self, instance_self, instance_class):
        return instance_self.__dict__.get(self.naming)


    def __delete__(self, instance_self, value):
        raise ValueError('read-only attribute')


class A:
    
    def __init__(self, a, b, c, init_y):
        self.a = a
        self.b = b
        self.c = c
        self.init_y = init_y
    
    init_y = Manager('init_y')
    
    def __str__(self):
        return f'{self.a}x{self.b}x{self.c} == {self.init_y}'
        
    special = Manager(10)
        
cls_a = A(1,4,7, 'bb_4321')
cls_b = A(1,4,7, 'bb_7351')
print(cls_a)
print(cls_b)
cls_a.init_y = 'ds_218221'
cls_b.init_y = 'ds_21822'


#===============================================================
#====================TASK 2=====================================
#===============================================================

class A:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __setattr__(self, attr_name, attr_value):
        if isinstance(attr_value, int):
            self.__dict__[attr_name] = attr_value
        else:
            raise ValueError('Soriamba, ints only')

#===============================================================
#====================TASK 3=simple==============================
#===============================================================

import datetime, uuid

class A:
    
    def __init__(self, a, b, c):

        self.identificator = uuid.uuid4()
        self.a = a
        self.b = b
        self.c = c

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        with open('log_x.txt', 'a') as text_file:
            text_file.write(f'{datetime.datetime.today()}\tValue set: "{value}"\tinstance key: "{self.identificator}"\n')
        self.__c = value


aa = A(1,7,88)
bb = A(24,67,90)
for x in range(1,30):
    aa.c = x
    bb.c = x**2


#===============================================================
#====================TASK 3=via descriptor======================
#===============================================================
#3) Реалізуйте властивість класу, яка володіє наступним
#функціоналом: при установці значення цієї властивості у файл із заздалегідь
#визначеною назвою повинен зберігатися час (коли встановлювали
#значення властивості) та встановлене значення.

import datetime, uuid

class Manager:
    
    def __init__(self, managed):
        self.managed = managed

    def __set__(self, instance_self, value):
        with open('field_c.txt', 'a') as text_file:
            if self.managed not in instance_self.__dict__:
                event = 'Initial assignation'
            else:
                event = 'Reassignation'
        
            text_file.write(f'{datetime.datetime.today()}\t{event}\t{value}\tInstance_key {instance_self.identificator}\n')
        
        instance_self.__dict__[self.managed] = value
        
    def __get__(self, instance_self, instance_class):
        return instance_self.__dict__.get(self.managed)


    def __delete__(self, instance_self, value):
        raise ValueError('read-only attribute')

class A:
    
    def __init__(self, a, b, c):

        self.identificator = uuid.uuid4()
        self.a = a
        self.b = b
        self.c = c
    
    c = Manager('c')


aa = A(1,7,88)
bb = A(24,67,90)
del aa.c
aa.c = 121312
