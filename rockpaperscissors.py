import random
player_total_wins = 0
computer_wins = 0

#the main function to run the program
def main():
    win_lose()

#input the number of rounds you want to play
def rounds():
    while True:
        try:
            total_rounds = int(input("Enter the total number of rounds you would like to play: "))
            break
        except ValueError:
            print("You must enter a number")
    
    return total_rounds

#count the wins to the player
def player_wins():
    global player_total_wins
    player_total_wins += 1
    return player_total_wins

#count the wins to the computer
def computer_wins_total():
    global computer_wins
    computer_wins += 1
    return computer_wins

#initialize the random number generator for the computer to make its choice
def computer_plays():
    computer_num = random.randint(1,3)
    if computer_num == 1:
        computer_num = "rock"
    if computer_num == 2:
        computer_num = "paper"
    if computer_num == 3:
        computer_num = "scissors"
    return computer_num

#the players input for what he wants
def player_input():
    player_input = ["rock", "paper", "scissors", "quit", "no", "yes"]
    player_choice = input("Enter rock, paper or scissors or if you want to quit, type quit: ")
    while player_choice not in player_input:
        print("try again thats not a correct input")
        break
    return player_choice

 #the main logic for the game  
def win_lose():
    while True:
        rounds_total = rounds()
        while rounds_total != 0:
            playerinput = player_input()
            comp_play = computer_plays()
            if playerinput == comp_play:
                print("It's a tie. Player chose", playerinput, "and the computer chose", comp_play, "Try again")
            elif playerinput == "rock":
                if comp_play == "scissors":
                    print("Player beats computer with", playerinput, "against", comp_play)
                    print("The total player wins is", player_wins())
                else:
                    print("computer beats Player with", comp_play, "against the players", playerinput)
                    print("The computer total wins is", computer_wins_total())
            elif playerinput == "paper":
                if comp_play == "rock":
                    print("Player beats computer with", playerinput, "against", comp_play)
                    print("The total player wins is", player_wins())
                else:
                    print("computer beats Player with", comp_play, "against the players", playerinput)
                    print("The computer total wins is", computer_wins_total())
            elif playerinput == "scissors":
                if comp_play == "paper":
                    print("Player beats computer with", playerinput, "against", comp_play)
                    print("The total player wins is", player_wins())
                else:
                    print("computer beats Player with", comp_play, "against the players", playerinput) 
                    print("The computer total wins is", computer_wins_total())
            if playerinput == "quit":
                print("quitting the game, goodbye!")
                break
            rounds_total -= 1
            print("There are", rounds_total, "rounds left")
        if player_total_wins > computer_wins:
            print("Player wins with", player_total_wins, "rounds won!")
        else:
            print("Computer wins with", computer_wins, "rounds won!")
        break
                        
main()