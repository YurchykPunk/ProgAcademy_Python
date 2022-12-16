from meatpiece import Pieceofmeat

class Student(Pieceofmeat):
    def __init__(self, university, id_card, average_mark, name, surname, sex, birth_year):
        super().__init__(name, surname, sex, birth_year)
        self.university = university
        self.id_card = id_card
        self.average_mark = average_mark
    def studinfo_short(self):
        return f'->{self.surname} {self.name}\t{self.id_card}'
    def title_only(self):
        return f'{self.surname} {self.name}'

    def details(self):
        return self.id_card, self.average_mark, self.name, self.surname, self.sex, self.birth_year

    def __str__(self):
        return f'Student {self.surname}/t{self.id_card}'