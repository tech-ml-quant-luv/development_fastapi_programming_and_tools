import random
import time

player_1_points = 0
player_2_points = 0
count = 1

def game_round(player_total_points):
    hold = False
    current_round_points = 0
    while not hold:
        player_input = input("Do you want to roll or hold? Press 'r' to roll or 'h' to hold: ")

        if player_input == "r":
            roll_outcome = random.choice(range(1,7))
            print(roll_outcome)
            if roll_outcome !=1:
                current_round_points += roll_outcome
            else:
                current_round_points = 0
                print(f"You Rolled {roll_outcome}, turn lost! ")
                hold = True
        else:
            player_total_points += current_round_points
            hold=True
    return player_total_points

while True:
    if max(player_1_points, player_2_points) >= 100:
        if player_1_points > player_2_points:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
        break
    elif count%2!=0:
        print("Player 1's chance!")
        player_1_points=game_round(player_1_points)
        print(f"Player 1 points after {count} rounds: {player_1_points}")
        time.sleep(1)
    else:
        print("Player 2's chance!")
        player_2_points = game_round(player_2_points)
        print(f"Player 2 points after {count} rounds: {player_2_points}")
        time.sleep(1)

    count +=1
