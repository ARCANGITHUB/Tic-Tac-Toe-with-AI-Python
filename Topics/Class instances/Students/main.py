class Student:

    def __init__(self, name, last_name, birth_year):
        self.student_id = str
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here

    def parameters(self):
        self.student_id = f"{self.name[0]}{self.last_name}{self.birth_year}"


daniel = Student(name=input(), last_name=input(), birth_year=input())
daniel.parameters()
print(daniel.student_id)
