class A:
    def say(self, smth):
        print(smth)
        
class B(A):
    ...

class C(A):
    def say(self, smth):
        print(f'{self} => {smth}')
    
class D(B, C):
    ...
    
    
_list = [
    A(),
    B(),
    B(),
    C(),
    D()
]

for x in _list:
    x.say(f'{x}')