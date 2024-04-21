 # can have any data types
myList=[1,"lisst"] 
len(myList)

#set all elements shold be unique, if we compare two ,order doesnt matter. even if 
mySet={1,2,3,5}
#order matters and we can change once created
mytuple=(1,2,3)

#Dictinaries
my_dict={
    
    "a":"ram",
    "ram":"jaganadh"
}
#membership operators in  not in

#control flow
a=True
if a==False:
    print(True)
else:
    print(False)
    
if a==True:
    print("Hello")
elif a==3: 
    print("come")
else:
    print("Done")
    
#For loops
b=[1,23,4,5]

for i in b:
    print(i)

for i in range(0,6):
    print(i)

# Functions

def MyBook():
    print("This is the Book")

def multiply(a,b):
    return a+b

print(multiply(1,3))

#Class

class Dog:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
        
    def speak(self):
        print(self.name+ ' says: Bark!')
        
print(my_dict["jam"])
        
    