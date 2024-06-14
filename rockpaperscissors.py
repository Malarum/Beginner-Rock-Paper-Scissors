import random

rounds = 0
player_wins = 0
computer_wins = 0

def main():
    player_input()
    
def computer_plays():
    computer_num = random.randint(1,3)
    if computer_num == 1:
        computer_num = "rock"
    if computer_num == 2:
        computer_num = "paper"
    if computer_num == 3:
        computer_num = "scissors"
    return computer_num

def player_input():
    while True:
        comp_play = computer_plays()
        player_choice = input("Enter rock, paper or scissors: ")
        if player_choice == "quit":
            break
        elif player_choice == comp_play:
            print("It's a tie. Player chose", player_choice, "and the computer chose", comp_play, "Try again")
        elif player_choice == "rock":
            print("you picked", player_choice)
            if comp_play == "scissors":
                print("Player beats computer with", player_choice, "against", comp_play)
            else:
                print("computer beats Player with", comp_play, "against the players", player_choice)
        elif player_choice == "paper":
            if comp_play == "rock":
                print("Player beats computer with", player_choice, "against", comp_play)
            else:
                print("computer beats Player with", comp_play, "against the players", player_choice)
        elif player_choice == "scissors":
            if comp_play == "paper":
                print("Player beats computer with", player_choice, "against", comp_play)
            else:
                print("computer beats Player with", comp_play, "against the players", player_choice)
        else:
            print("invalid choice please try again")
        



main()