class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.instance = self.name[0] + self.last_name + self.birth_year


_name = input().strip()
_last_name = input().strip()
_birth_year = input().strip()

student = Student(_name, _last_name, _birth_year)
print(student.instance)
