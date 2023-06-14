class Human:
    name:str
    father_name:str
    age:int
    posXY:tuple[int, int]    
        
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.father_name = kwargs.get('father_name')
        self.age = kwargs.get('age')
        self.posXY = kwargs.get('posXY')
        
    def spell_words(self, text):
        print(f'{self.name} said: {text}')
    
    def walk_to(self, point):
        self.posXY = point
        

