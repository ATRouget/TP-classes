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

    def load_grades_from_file(self, filename: str):
        with open(filename, 'r', encoding = 'utf-8') as file :
            for line in file :
                tuple = line.strip().split(',')
                first_name, last_name = tuple[0], tuple[1]
                topic = tuple[2]
                notes = tuple[3:]
                student = self.pupils[first_name + " " + last_name]
                for n in notes :
                    student.add_grade(topic, float(n))
    
    def catalog(self):
        C = {}
        for eleve in self.pupils :
            matières = self.pupils[eleve].followed_topics()
            for m in matières :
                if m in C :
                    C[m] = C[m] + 1
                else :
                    C[m] = 1
        return C


