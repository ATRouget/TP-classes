from collections import defaultdict
from TP_classes_students import Student

class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.pupils = {}

    def add_student(self, student: Student):
        self.pupils[student.first_name + " " + student.last_name] = student

    def __len__(self):
        return len(list(self.pupils.keys()))

    def __repr__(self):
        return "Class " + self.classname + " - " + f"{len(self)}" + " student(s)"

    def get_student(self, first_name: str, last_name:str):
        if first_name + " " + last_name in self.pupils :
            return self.pupils[first_name + " " + last_name]
        else :
            return None
        
    def load_students_from_file(self, filename: str) :
        with open(filename, 'r', encoding = 'utf-8') as file :
            for line in file :
                first_name, last_name = line.strip().split(',')
                student = Student(first_name, last_name)
                self.add_student(student)



