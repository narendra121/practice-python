myList=[1,2,4,6,"hello"]
print(myList)
print(myList[0:len(myList):2])

myList.append(6)
print(myList)

myList.insert(3,"some")
print(myList)

myList.remove("some")
print(myList)

myList.pop()
print(myList)



#Sets
#if we convert list to set thaen it will have unique values
#set not allowed to slice
#order not guaranteed
mySet={1,2,3,4,5,5}
print(mySet)
mySet.add(5)
len(mySet)
mySet.discard(1)

#tuples
#can be sliced but cant be modified
myTuple=(1,2,3)
myTuple[0]


#dict

animals={
    "cat":"mew",
    "dog":"bow"
}
print(animals)
print(animals["cat"])
animals["cat"]= "mew mew"
print(animals)
print(animals.keys())
print(animals.values())

print(animals.get("cat"))
print(len(animals))


#List Comprehension
#like having filter
compList=[1,2,3,4,5]
[2*item for item in compList]
filtered=[item for item in compList if item%10==0]

def cleaner(word):
    return word.replace(".","").lower()
mystr="hello name. ram."
[cleaner(word) for word in mystr.split()]


#dict comprehension

animalList=[(1,1),(2,2)]

animals={key:value for key, value in animalList}
print(animals)
list(animals.items())

[{"letter":key, "name":value} for key, value in animals.items()]