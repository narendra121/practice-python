# file=open("my_file.txt")
# content=file.read()
# print(content)
# file.close()

with open("my_file.txt") as file:
    contents=file.read()
    print(contents)
    
with open("my_file.txt",mode="a") as file:
    file.write("rome")
    
