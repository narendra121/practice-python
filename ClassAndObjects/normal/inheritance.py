class Animal:
    def __init__(self):
        self.num_eyes=2
    
    def breath(self):
        print("i inhale, exhale")
        
class Fish(Animal):
    
    def __init__(self):
        super().__init__() #inherit
    
    def swim(self):
        print("moving in water")
    
    def breathe(self):
        super().breath() #takes parent and execute own too
        print("doing this under water")

nemo= Fish()
nemo.swim()
nemo.breath()