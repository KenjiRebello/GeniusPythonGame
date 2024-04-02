import os
import random
import time

# In Brazil, we call Simon Game as Genius, so i'll use the name Genius here

# Clear screen logic
# In case the OS is Windows, it will clear the screen with cls, otherwise it will use clear (NOTE: In Windows 11, both will work)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Usable colors
colors = ("R", "B", "Y", "G")

# Genius Bot
genius_bot = []

# Player Score
score = 0