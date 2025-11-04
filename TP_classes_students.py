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

    def report(self):
            """ génère un rapport formaté des moyennes par matière """
            report_lines = []
            header = f"Report for student {self.first_name} {self.last_name}"
            report_lines.append(header)
            report_lines.append("+===============+===============+")
            report_lines.append("|     Topic     |    Average    |")
            report_lines.append("+===============+===============+")
        
            for topic in self.followed_topics():
                average = self.compute_average(topic)
                report_lines.append(f"|  {topic:<13}|    {average:>6.2f}     |") # Format topic left-aligned in 13 spaces, average right-aligned in 6 spaces with 2 decimals
                report_lines.append("+---------------+---------------+")
        
            return "\n".join(report_lines) # \n permet de retourner à la ligne
