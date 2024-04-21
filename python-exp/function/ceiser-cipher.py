alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    res=""
    for letter in text:
        letterIdx=alphabet.index(letter)
        eryIdx=(shift+letterIdx+1)%26
        res+=alphabet[eryIdx-1]
    print(res)
    
def dencrypt(text ,shift):
    res=""
    for letter in text:
        letterIdx=alphabet.index(letter)
        eryIdx=(letterIdx+1-shift)%26
        res+=alphabet[eryIdx-1]
    print(res)

if direction=="encode":
    encrypt(text,shift)
elif direction =="decode":
    dencrypt(text,shift)