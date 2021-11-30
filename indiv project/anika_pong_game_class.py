# Anika Bajpai
# ACADEMIC INTEGRITY STATEMENT
# I have not used source code obtained from any other unauthorized
# source, either modified or unmodified. Neither have I provided
# access to my code to another. The project I am submitting
# is my own original work.
# ===============================================================================
import pygame
import anika_pong_variables
from anika_pong import screen_measure
import sys

class Game():
    def __init__(self): #initializes game itself
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 40) #font configuration
        self.background = pygame.Surface(screen_measure.get_size()).convert() #fill background
        self.clock = pygame.time.Clock() # initialize clock
    def quit(self):
        sys.exit(0)
        pygame.quit()

