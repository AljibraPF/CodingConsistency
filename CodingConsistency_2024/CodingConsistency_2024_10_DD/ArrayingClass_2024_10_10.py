#Arrays and OOP

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.get_average():.2f}")

student1 = Student("Al")

student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

student1.display_info()
