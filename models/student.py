from . import Human


class Student(Human):
    school:str
    marks:list[int] = []
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.marks = kwargs.get('marks')
        self.school = kwargs.get('school')
        
    def learn(self, subject):
        ...
    
    def spell_words(self, subject, text):
        return super().spell_words(f'{subject} => {text}')
        