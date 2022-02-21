import random
import sys

player_score, computer_score, ties = 0, 0, 0


def print_score(player_score, computer_score, ties):
    print("\n SCOREBOARD")
    print("You won " + str(player_score) + " times")
    print("The computer won " + str(computer_score) + " times")
    print("There has been " + str(ties) + " ties\n")


def game(player_score, computer_score, ties):
    player_option = input("Enter \"rock\", \"paper\" or \"scissors\": ").strip()
    options = ["rock", "paper", "scissors"]
    computer_option = random.choice(options)
    winning_condition = player_option == options[0] and computer_option == options[2] or player_option == options[
        1] and computer_option == options[0] or player_option == options[2] and computer_option == options[1]

    tie_condition = player_option == computer_option

    losing_condition = player_option == options[2] and computer_option == options[0] or player_option == options[
        0] and computer_option == options[1] or player_option == options[1] and computer_option == options[2]

    if winning_condition:
        print("You win!")

        player_score += 1
        print_score(player_score, computer_score, ties)

    elif tie_condition:
        print("It's a tie!")
        ties += 1
        print_score(player_score, computer_score, ties)
    elif losing_condition:
        print("Better luck next time ):")
        computer_score += 1
        print_score(player_score, computer_score, ties)
    option_continue = input("Do you want play again(yes/no)")
    if option_continue == "yes":
        game(player_score, computer_score, ties)
    else:
        sys.exit()


game(player_score, computer_score, ties)
