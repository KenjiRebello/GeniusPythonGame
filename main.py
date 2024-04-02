import os
import random
import time

# In Brazil, we call Simon Game as Genius, so i'll use the name Genius here

# Clear screen logic
# In case the OS is Windows, it will clear the screen with cls, otherwise it will use clear (NOTE: In Windows 11, both will work)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Genius Colors
def geniusColor():
    global genius_bot
    genius_bot += random.choice(colors)

# Player's Turn
def playerTurn():
    turn = input("Your Turn: ".upper)
    return turn

# Player Current Score
def playerScore():
    print("Score: ", score)

# Genius Difficulty
# Here i try to create a logic to make the game harder or easier for the player (Very ugly coding, i know)
def geniusDifficulty():
    difficulty = int(input("How hard do you want the Genius Bot to be? \n 3 - Easy \n 2 - Medium \n 1 - Hard \n"))

    if difficulty == 1:
       difficulty = 0.1

    elif difficulty == 2:
       difficulty = 0.3

    elif difficulty == 3:
       difficulty = 0.5
    else:
      print("Only numbers allowed! \n Closing the game...")

    return difficulty

# Usable colors
colors = ("R", "B", "Y", "G")

# Genius Bot
genius_bot = []

# Genius Sequence
for i in range(1):
    genius_bot += random.choice(colors)

# Player Score
score = 0

# Show Best Score
clear()
playerScore()
time.sleep(4)

