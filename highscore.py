import highscore
# Here is the logic to make file reading to highscore.txt and saving the High Score in the game

#Fuction that gets the High Score in highscore.txt
def getHighScore():
    with open("highscore.txt", "r") as hs:
        bigScore = hs.readlines()
        return bigScore
    
#Function that sets the High Score in highscore.txt    
def setHighScore(name, score):
    with open("highscore.txt", "w") as hs:
        hs.write(name, "\n")
        hs.write(score)

# The values for High Score
record = getHighScore()
highname = record[0]
bigScore = int(record[1])