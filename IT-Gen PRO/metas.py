class MyMetaClass(type):
    def __new__(typeclass, classname, supers, classdict):
        with open('class_base.txt', 'a') as cb:

            cb.write(f'"{classname}"\n{classdict}\n\n')

        return type.__new__(typeclass, classname, supers, classdict)
    
    def __init__(cls, classname, supers, classdict):
        pass
    
        
class Cat(metaclass=MyMetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        return 'party'

class Dog(metaclass=MyMetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        return 'party'
    
aa = Cat('Zozo', 12)
aa = Cat('Zozo', 14)
aa = Cat('Zozo', 19)
