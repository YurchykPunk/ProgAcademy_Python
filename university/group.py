from student import Student
import excepts
import log_mod

class Studygroup:
    def __init__(self, groupname, studlimit=10):
        self.groupname = groupname
        self.group = []
        self.studlimit = studlimit
        
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError()
        
        if len(self.group) == self.studlimit:
            raise excepts.CapacityError(self.groupname, self.studlimit)
        
        if student in self.group:
            raise excepts.DuplicateError(student.title_only(), self.groupname)
        
        self.group.append(student)
        log_mod.logger.info(f'Modulename:"{__class__.__name__}".' \
            f'Student "{student.surname} {student.name[0]}:" succesfully added to group {self.groupname}')
        return self
    
    def del_student(self, student):
        if student.id_card in list(map(lambda x: x.id_card, self.group)):
            self.group.remove(student)
            return self
        else:
            return False
    
    def groupinfo(self):
        return '\n'.join(list(map(lambda x: f'{x.surname} {x.name[0]}. ID Card {x.id_card}. Average mark: {x.average_mark}', self.group)))

    def find_student(self, sur):
        check_gen = []
        for idx, x in enumerate(self.group):
            check_gen.append(f'{self.group[idx].studinfo_short()}') if x.surname == sur else False
        res = '\n'.join(check_gen)
        return res and f'Following students were found:\n{res}' or False
    
    def __str__(self):
        return '\n'.join(list(map(lambda x: f'{x.surname} {x.name[0]}.', self.group)))
