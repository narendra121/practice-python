from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
bidding_db={}

def ManageBid(name,bid,display):
    if display=="yes":
        bidding_db[name]=bid
    elif display=="no":
        winner=""
        highest_bid=0
        for name in bidding_db:
            if bidding_db[name]>highest_bid:
                highest_bid=bidding_db[name]
                winner=name
        print(f"The winner is {winner} with a bid of {highest_bid}")

print(art.logo)
print("Welcome to the secret aution program")
display="yes"
while display=="yes":
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: "))
    ManageBid(name,bid,display)
    display=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

if display=="no":
    ManageBid(0,0,display)