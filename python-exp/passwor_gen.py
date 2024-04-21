# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P

lt = "".join(random.choices(letters, k=nr_letters))
sym = "".join(random.choices(symbols, k=nr_symbols))
num = "".join(random.choices(numbers, k=nr_numbers))

# Concatenate the strings
all_characters = lt + sym + num
print(all_characters)
# Convert the string to a list and shuffle
shuffled_characters = list(all_characters)
random.shuffle(shuffled_characters)

# Convert the list back to a string
shuffled_password = ''.join(shuffled_characters)

print(shuffled_password)
