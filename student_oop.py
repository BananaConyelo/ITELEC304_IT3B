class Student:
    def __init__(self, name, age, course, year_level):
        self.name = name
        self.age = age
        self.course = course
        self.year_level = year_level
    
    def study(self):
        print(f'{self.name} is studying ...')

    def get_info(self):
        return f'Name {self.name}, Age {self.age}, Course {self.course}, Year Level {self.year_level}'
    
    def take_exam(self):
        score = input("Type your score")
        print(f'{self.name} got {score} points in ITELEC304')
    
    
student1 = Student("Ana", 20, "BSIT", "4th Year")
student2 = Student("Jessie", 21, "BSPA", "2nd Year")


print(student1.get_info())
student2.study()
student2.take_exam()
