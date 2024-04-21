class User:#name is Pascal case 
    def __init__(self,name):#constructor
        print("Im constructor")
        self.name=name
    
    def enterSeats(self,seats):
        self.seats=seats
        
user1= User("narendra")

print(user1)