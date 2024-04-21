
from artist import art
import data
import random


def Game():
    score=0
    win=True
    while win:
        choice1=random.choices(data.data,k=1)
        choice2=random.choices(data.data,k=1)
        print(art.logo)
        print(f"Compare A: {choice1[0].get('name')}, {choice1[0].get('description')}, from {choice1[0].get('country')}.")
        print(art.vs)
        print(f"Compare B: {choice2[0].get('name')}, {choice2[0].get('description')}, from {choice2[0].get('country')}.")
        guess=input("Who has more followers? Type 'A' or 'B': ")
        if guess=="A" and choice1[0].get('follower_count')>choice2[0].get('follower_count'):
            win=True
        elif guess=="B" and choice1[0].get('follower_count')<choice2[0].get('follower_count'):
            win=True
        else:
            win=False
            break
        score=score+1
    print(f"Your Score Is : {score}")
Game()