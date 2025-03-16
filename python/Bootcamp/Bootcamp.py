import random

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    options = ["rock","papper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "Its a tie!"
    
    elif player == "rock" :
        if computer == "scissors":
            return "Rock smashes scissor! You win!"
        else:
            return "Paper Covers rock! you lose"

    elif player == "paper" :
        if computer == "rock":
            return "paper covers rock! You win!"
        else:
            return "scissors cut paper! you lose"

    elif player == "scissors" :
        if computer == "paper":
            return "Scissora cut paper! You win!"
        else:
            return "Rock smaches scissors! You lose"        
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"] )
print(result)


#fstring:- it allows you to make strings with variabs in another pyton code
#Ex:-

age = 25
print(f"Jim is {age} years old.")

def greeting():
    return "hi"

#Dictionary:- Dictionary in python are used to store key value pairs

dict = {"name":"beau", "color": choices} 

#list:- list is used to store multiple items in single variables

food = ["pizza","carrots","eggs"]
dinner = random.choice(food)