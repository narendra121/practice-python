#class


class Dog:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
        
    def speak(self):
        print(self.name+ ' says: Bark!')
  
myDog= Dog("jam",4)

#static and intance methods


class WordSet:
    def __init__(self):
        self.words=set()
    def addText(self,text):
        text=WordSet.cleanText(text)
    def cleanText(text):#static method
        text=text.replace("!","").replace(".","")
        return text.lower()
wordSet=WordSet()
wordSet.addText()


class WordSet:
    def __init__(self):
        self.words=set()
    def addText(self,text):
        text=self.cleanText(text)
    @staticmethod#decorTORS
    def cleanText(text):#static method
        text=text.replace("!","").replace(".","")
        return text.lower()
wordSet=WordSet()
wordSet.addText()


#INHERITANCE

class Dog:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
        
    def speak(self):
        print(self.name+ ' says: Bark!')
  
class Domination(Dog):
    def speak(self):#overiding
        print("yup yup")
        
    def wagTail(self):
        print("waging")
        
        
#extent builtin       
myList=list()

class UniqueList(list):
    def append(self, item) :
       if item in self:
           return
       super().append(item)#call parent method
       
       
class UniqueList(list):
    def __init__(self):
        super().__int__()#call the parent first then ours
        self.some='unique'
    def append(self, item) :
       if item in self:
           return
       super().append(item)#call parent method
       