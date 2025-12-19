#--importing the random module--
import random
#--creating the variables, and the tuple
choices = ("rock", "paper", "scissors")
print("Welcome to Rock paper scissors\nTry to beat the computer!")
user_score = 0
computer_score = 0
#--the main game--
while True:
    #--prepares the answer of the computer--
    computer_answer = random.choice(choices)
    #--gets the answer of the user--
    answer = input("Your answer:(rock, paper, scissors)")
    #---checks the user's answer--
    if answer in choices:
        #--evaluates who won--
        if answer == "rock":
            if computer_answer == "paper":
                print("The computer one! computer played:", computer_answer)
                computer_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "scissors":
                print("The user won! computer played:", computer_answer)
                user_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "rock":
                print("It's a tie! computer played:", computer_answer)
                print(f'computer:{computer_score}, user:{user_score}.')
        elif answer == "paper":
            if computer_answer == "paper":
                print("It's a tie! computer played:", computer_answer)
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "scissors":
                print("The computer one! computer played:", computer_answer)
                computer_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "rock":
                print("The user won! computer played:", computer_answer)
                user_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
        elif answer == "scissors":
            if computer_answer == "paper":
                print("The user won! computer played:", computer_answer)
                user_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "scissors":
                print("It's a tie! computer played:", computer_answer)
                print(f'computer:{computer_score}, user:{user_score}.')
            elif computer_answer == "rock":
                print("The computer one! computer played:", computer_answer)
                computer_score += 1
                print(f'computer:{computer_score}, user:{user_score}.')
    else:
        #--prints invalid if the user inputted an invalid answer--
        print("Invalid input!")
#Made using vscode
#Made by geneloclwg
