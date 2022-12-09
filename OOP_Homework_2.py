#Домашнє завдання:
#1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
#2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
#3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
#Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
#Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

import random

class Pieceofmeat:
    def __init__(self, name, surname, sex, birth_year):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.birth_year = birth_year
    
    def details(self):
        return self.name, self.surname, self.sex, self.birth_year
    
    def __str__(self):
        return f'Mr(s) {self.surname}, {self.name}'
        
class Student(Pieceofmeat):
    def __init__(self, university, id_card, average_mark, name, surname, sex, birth_year):
        super().__init__(name, surname, sex, birth_year)
        self.university = university
        self.id_card = id_card
        self.average_mark = average_mark
    def studinfo_short(self):
        return f'->{self.surname} {self.name}\t{self.id_card}'

    def details(self):
        return self.id_card, self.average_mark, self.name, self.surname, self.sex, self.birth_year

    def __str__(self):
        return f'Student {self.surname}/t{self.id_card}'
        
h_names = ['George','Harry','Ronald','Seamus','Rose','Luna','Angelina']
q_n = len(h_names)
h_surnames = ['Weasley','Potter','Lovegood','Finnigan','Wood','Creevey']
q_s = len(h_surnames)
human_creator = [Pieceofmeat(h_names[random.randint(0,q_n-1)],h_surnames[random.randint(0,q_s-1)],'',random.randint(1994,1998)) for x in range(50)]
#sex corrector
for x in human_creator:
    x.sex = h_names.index(x.name) > 3 and 'F' or 'M'

student_list = []
for index, x in enumerate(human_creator):
    student_unit = Student('Hogwarts', f'2022-12-523/{index}', random.randint(55,100),x.name, x.surname, x.sex, x.birth_year)
    student_list.append(student_unit)

class Studygroup:
    def __init__(self, groupname):
        self.groupname = groupname
        self.group = []
        self.STUDLIMIT = 10
        
    def add_student(self, student):
        if len(self.group) < self.STUDLIMIT and not student.id_card in list(map(lambda x: x.id_card, self.group)):
            self.group.append(student)
        else:
            return False
        return self
    
    def del_student(self, student):
        if student.id_card in list(map(lambda x: x.id_card, self.group)):
            self.group.remove(student)
        else:
            return False
        return self
    
    def groupinfo(self):
        return '\n'.join(list(map(lambda x: f'{x.surname} {x.name[0]}. ID Card {x.id_card}. Average mark: {x.average_mark}', self.group)))

    def find_student(self, sur):
        check_gen = []
        for idx, x in enumerate(self.group):
            check_gen.append(f'{self.group[idx].studinfo_short()}') if x.surname == sur else False
        res = '\n'.join(check_gen)
        return res and f'Following students were found:\n{res}' or 'No students found'
    
    def __str__(self):
        return '\n'.join(list(map(lambda x: f'{x.surname} {x.name[0]}.', self.group)))

it_gen = Studygroup('It-Gen group')

for x in range(14):
    it_gen.add_student(student_list[x])
it_gen.del_student(student_list[3])

print(it_gen.find_student('Potter'))
print(it_gen)
print(student_list[3].details())
