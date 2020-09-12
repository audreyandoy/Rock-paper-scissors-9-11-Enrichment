import random
# Project planning
# 2 players: player vs. computer
# 1) ask player for their choice
# either chooses from rock paper or scissors
# 2) computer randomly makes choice
# 3) printing both inputs
# 4) Outputting/Comparing who won:
# paper beats rock
# scissors beats paper
# rock beats scissors

print("***WELCOME TO ROCK PAPER SCISSORS SHOWDOWN***")

choices = ["rock", "paper", "scissors"]

player_choice = input("Choose rock, paper, or scissors: \n") 
print(f"Player Choice: {player_choice}")

while player_choice not in choices:
    player_choice = input("Not valid. Please choose rock, paper, or scissors: \n") 
print(f"Player Choice: {player_choice}")


