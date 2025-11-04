from collections import defaultdict
from TP_classes_students import Student

class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.pupils = {}

    def add_student(self, student: Student):
        self.pupils[student] = 1

    def __len__(self):
        return len(list(self.pupils.keys()))

    def __repr__(self):
        return "Class " + self.classname + " - " + f"{len(self)}" + " student(s)"

try:
    classe = Class("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    print (repr(classe))
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    if repr(classe) != "Class P20 - 1 student(s)":
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

