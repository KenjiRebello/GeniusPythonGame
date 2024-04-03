import os
import random
import time
import signal
import sys

# In Brazil, we call Simon Game as Genius, so i'll use the name Genius here

# Removes the CTRL+C ugly error and gives a Good Bye instead
def signal_handler(sig, frame):
    sys.stdout.write('\r')
    sys.stdout.write(' ' * 80)
    sys.stdout.write('\r')
    print('Good Bye o/ \nThanks for Playing!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Clear screen logic
# In case the OS is Windows, it will clear the screen with cls, otherwise it will use clear (NOTE: In Windows 11, both will work)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function that gets the High Score
def getHighScore():
    with open("highscore.txt", "r") as hs:
        bigScore = hs.readlines()
    return bigScore

# Function that shows the HighScore
def showHighScore():
    print(f"High Score:  {highscore} by {highname}")
    
# Function that sets the High Score in highscore.txt    
def setHighScore(name, score):
    with open("highscore.txt", "w") as hs:
        hs.write(f"{name} \n {score}")

# This creates the highscore.txt in case doesn't exists
try:
    getHighScore()
except:
    with open("highscore.txt", "w") as f:
        f.write("null\n0")

# The values for High Score
record = getHighScore()
highname = record[0]
highscore = int(record[1])


# Genius Colors
def geniusColor():
    global genius_bot
    genius_bot += random.choice(colors)

# Player's Turn
def playerTurn():
    turn = input("Your Turn: ").upper()
    return turn

# Player Current Score
def playerScore():
    print("Score: ", score)

# Genius Difficulty
# Here i create a logic to make the game harder or easier for the player (Very ugly coding, i know)
difficulty = int(input("How hard do you want the Genius Bot to be? \n ONLY NUMBERS \n 3 - Easy \n 2 - Medium \n 1 - Hard \n"))

if difficulty == 1:
   difficulty = 0.1

elif difficulty == 2:
   difficulty = 0.3

elif difficulty == 3:
   difficulty = 0.5

# Usable colors
colors = ("R", "B", "Y", "G")

# Genius Bot
genius_bot = []

# Genius Sequence
for i in range(2):
    geniusColor()

# Player Score
score = 0

# Show Best Score
clear()
playerScore()
time.sleep(2)

# Here's the gameplay
while True:

# Adding color to the sequence
    geniusColor()

# Combine Genious color to String
    sequence = "".join(genius_bot)

# Showing before printing
    print("Genius_bot Color: ")
    time.sleep(difficulty)
    clear()
    playerScore()

# Showing Colors
    for color in genius_bot:

        # Between Colors
        print("Genius_bot Color: ")
        time.sleep(difficulty)
        clear()
        playerScore()

        # Show Next Color
        print("Genius_bot Color: ", color)
        time.sleep(1)
        clear()
        playerScore()

# Get Input and Compare to Genius
    if playerTurn() == sequence:

        # Score
        score += 1
        clear()
        playerScore()

        # Game Over screen
    else:
        # Checks if current score is higher than the high score
        if score > highscore:

            # GAME OVER text
            clear()
            print("GAME OVER \nNew High Score!!!! \n ", score)

            # Player inputs his name
            name = input("Enter you name:")

            # Save high score and end game
            setHighScore(name, str(score))
            break
        
        #If it isn't higher than the current high score, ends game and show high score
        else:
            clear()
            print("GAME OVER")

            getHighScore()

            print("Score: ", score)
            break
