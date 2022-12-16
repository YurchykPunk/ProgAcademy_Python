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