#Домашнє завдання:
#1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
#2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
#3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
#Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
#Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.

import random
import meatpiece
import student
import group

        
h_names = ['George','Harry','Ronald','Seamus','Rose','Luna','Angelina']
q_n = len(h_names)
h_surnames = ['Weasley','Potter','Lovegood','Finnigan','Wood','Creevey']
q_s = len(h_surnames)
human_creator = [meatpiece.Pieceofmeat(h_names[random.randint(0,q_n-1)],h_surnames[random.randint(0,q_s-1)],'',random.randint(1994,1998)) for x in range(50)]
#sex corrector
for x in human_creator:
    x.sex = h_names.index(x.name) > 3 and 'F' or 'M'

student_list = []
for index, x in enumerate(human_creator):
    student_unit = student.Student('Hogwarts', f'2022-12-523/{index}', random.randint(55,100),x.name, x.surname, x.sex, x.birth_year)
    student_list.append(student_unit)



it_gen = group.Studygroup('It-Gen group')
for x in range(8):
    it_gen.add_student(student_list[x])
it_gen.del_student(student_list[3])

it_gen.add_student(student_list[2])

print(it_gen.find_student('Potter'))
print(it_gen)
print(student_list[3].details())