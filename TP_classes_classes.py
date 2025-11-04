from collections import defaultdict
from TP_classes_students import student

class Class:
    def __init__(self, classname: str):
        self.classname = classname
        self.pupils = defaultdict(list)

    def add_student(self, student: Student):
        

    def __len__(self):
        return 0

    def __repr__(self):
        return f""