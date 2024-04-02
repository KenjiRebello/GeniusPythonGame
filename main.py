import os
import random
import time

#Clear screen logic
def clear():
    #In case the OS is Windows, it will clear the screen with cls, otherwise it will use clear (NOTE: In Windows 11, both will work)
    os.system('cls' if os.name == 'nt' else 'clear')
