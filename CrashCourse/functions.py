#Func

def add(num1,num2):
    return num1+num2

add(1,2)
def add(num1,num2=2):
    return num1+num2
add(1)
def add(num1,num2):
    return num1+num2
add(num1=1,num2=3)

#multiple args
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


def add(*args,**kwargs):
    sum=0
    for i in args:
        sum+=i
    return sum


#lambda function

(lambda x: x+3)(5)