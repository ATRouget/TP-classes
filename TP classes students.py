from collections import defaultdict
class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}
        #self.grades = defaultdict(list)
        #possible aussi, dans ce cas pas besoin de tester si la clef existe déjà pour ajouter une note

    def __repr__(self):
        return self.first_name+" "+self.last_name
    
    def add_grade(self, topic: str, grade: float) -> None:
        if grade > 20 or grade < 0 :
            raise ValueError("Grade must be between 0 and 20")
        if topic in self.grades :
            self.grades[topic].append(grade)
        else:
            self.grades[topic] = [grade]
    
    def followed_topics(self) -> list :
        return list(self.grades.keys()) #dict.keys() renvoie un dictionnaire
    
    def compute_average(self, topic: str) -> float :
        if topic in self.grades :
            return sum(self.grades[topic])/len(self.grades[topic])
        else :
            return -1


try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    if (student.compute_average("History") != 11.):
        raise Exception("Issue in your average calculation.")
    if (student.compute_average("French") != -1.):
        raise Exception("If topic is not followed return -1")
except Exception as e:
    print('OOPS - There is an issue in your compute_average method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
