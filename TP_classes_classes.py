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





try:
    classe = Class("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    new_student = classe.get_student("Matthieu", "Mazière")
    assert student == new_student
    new_student = classe.get_student("Jérôme", "Adnot")
    assert new_student is None
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

