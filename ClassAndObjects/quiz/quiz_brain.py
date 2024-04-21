
class QuestionBrain:
    def __init__(self,qlist):
        self.qno=0
        self.qlist=qlist
    
    def next_question(self):
        if self.qno==len(self.qlist)-1 :
            return ""
        question=self.qlist[self.qno]
        self.qno+=1
        input(f"Q.{self.qno}: {question.text} ? (True/False):")
    