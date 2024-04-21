from decimal import Decimal,getcontext
a=0
b=0.1001

print(type(a))
print(type(b))
print(round(b,4))

getcontext().prec=2
res=Decimal(1)/Decimal(3)
print(res)

#Boolean
myList=[1,2]

if myList:
    print("my list has some values")
    
#strings

name= "my name is narendra"
print(name[0])
print(name[0:7])
print(len(name))

first="my number is :"+str(5)
print(first)

second=f"my number is {5}"
print(second)

third= "my number is {}".format(5)
print(third)

multiLine="""
        Hello man
        you are done
"""
print(multiLine)


#Bytes

by=bytes(4)
print(by)

print(int('A2',16))