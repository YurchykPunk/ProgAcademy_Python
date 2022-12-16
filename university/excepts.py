class CapacityError(Exception):
    def __init__(self, group_title, limit):
        
        self.group_title = group_title
        self.limit = limit
        
    def __str__(self):
        return f'The group {self.group_title} is overbooked! Maximum students number is {self.limit}'
        
class DuplicateError(Exception):
    def __init__(self, stud_name, group_name):
        
        self.stud_name = stud_name
        self.group_name = group_name
        
    def __str__(self):
        return f'The student {self.stud_name} is already in group "{self.group_name}"'