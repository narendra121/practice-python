# *args

def add(*args):
    for n in args:
        print(n)
        
add(3,4,6)

def calculate(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(key,val)
calculate(add=3,hello=0)