#Step 2

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

print(f'{hangman_art.logo}')

print(f'Pssst, the solution is {chosen_word}.')

disp=[]
length=len(chosen_word)
count=length
my_array = ["-"] * length
lives=6

while (count>0 and lives>=0):
    guess = input("Guess a letter: ").lower()
    found=False
    for i in range(0,length):
        if chosen_word[i] == guess :  
          found=True
          if  my_array[i]=="-" :     
            my_array[i]=guess
            count=count-1
          else:
            print("You already guessed lettter "+guess)
            break
    
    if  not found  :
        print("Your opted letter "+guess+" is not present in the word")
        print(f"{hangman_art.stages[lives]}")
        lives=lives-1 
        
    print(my_array)
    
if lives<0:
    print(f"You Lost !")
elif lives>=0:
    print(f"You Won !")