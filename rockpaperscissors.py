import random

rounds = 0
player_wins = 0
computer_wins = 0
#while quit is not written and the rounds are less than 5 the program runs
while True and rounds < 5:
    #initialize the random number generator and set the rock paper and scissors
    computer_plays = random.randint(1,3)
    if computer_plays == 1:
        computer_plays = "rock"
    if computer_plays == 2:
        computer_plays = "paper"
    if computer_plays == 3:
        computer_plays = "scissors"
    #enter in the user commands. if quit is selected the game will quit.
    usr_command = input("Enter rock, paper, or scissors: ")
    if usr_command == "quit":
        print("quitting the game. Goodbye!")
        break
    #start of the game logic. determines the winner based on the choices made
    elif usr_command == computer_plays:
        print("its a tie player chose", usr_command, "and computer chose", computer_plays, "try again")
    elif usr_command == "rock": 
        print("You picked: " + usr_command)
        if computer_plays == "scissors":
            print("player wins with ", usr_command, "against the computers", computer_plays)
            player_wins += 1
        else:
            print("computer wins")
            computer_wins += 1
        rounds += 1
    elif usr_command == "paper":
        print("You picked: " + usr_command)
        if computer_plays == "rock":
            print("player wins with ", usr_command, "against the computers", computer_plays)
            player_wins += 1
        else:
            print("player loses with ", usr_command, "against the computers", computer_plays)
            computer_wins += 1
        rounds += 1
    elif usr_command == "scissors":
        print("You picked: " + usr_command)
        if computer_plays == "paper":
            print("player wins with ", usr_command, "against the computers", computer_plays)
            player_wins += 1
        else:
            print("player loses with ", usr_command, "against the computers ", computer_plays)
            computer_wins += 1
        rounds += 1
    else:
        print("invalid choice. please try again")
    #printing the winning statements
    print("player has won ", player_wins, "round and the computer has won", computer_wins, " rounds there have been ", rounds, " rounds")
    if player_wins == 3:
        print("player wins best 3 out of 5")
        break
    elif computer_wins == 3:
        print("computer wins best 3 out of 5")
        break
    if rounds == 5:
        print("game is over.")
        break
    