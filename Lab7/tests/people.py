class Person: 
    def __init__(self, name): 
        self.name = name 
    def introduce(self): 
        return f"Hi, I'm {self.name}." 
    pass 


class Student(Person): 
    def __init__(self, name): 
        super().__init__(name) 
        self.scores = [] 
    def add_score(self, score): 
        self.scores.append(score) 
    def average(self): 
        if len(self.scores) == 0: 
            return 0 
        return sum(self.scores) / len(self.scores) 

    def introduce(self): 
        return f"Hi, I'm {self.name}, a student."



class Instructor(Person): 
    def __init__(self, name, department): 
        super().__init__(name)
        self.department = department 
    def introduce(self): 
        return f"Hi, I'm {self.name} and I teach {self.department}."
