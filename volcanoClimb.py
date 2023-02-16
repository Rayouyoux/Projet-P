'''
IMPORTS
'''
import pygame
from sys import exit



'''
VARIABLES
'''
pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Volcano Climb')
clock = pygame.time.Clock()



'''
FUNCTIONS
'''



'''
GAME INITIALIZATION
'''



'''
GAME LOOP
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    pygame.display.update()
    clock.tick(60)