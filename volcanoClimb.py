'''
IMPORTS
'''
from random import choice
import pygame
from sys import exit



'''
VARIABLES
'''
pygame.init()
screenWidth = 640
screenHeight = 960
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Volcano Climb')
clock = pygame.time.Clock()

'''
SURFACES
'''
# Setting Default Image Size
DEFAULT_IMAGE_SIZE = (64, 64)

# Background & Resizing & Rotating
backgroundLeftSurface = pygame.image.load('background/cotegauche.png')
backgroundLeftSurface = pygame.transform.scale(backgroundLeftSurface, DEFAULT_IMAGE_SIZE)

backgroundCenterSurface = pygame.image.load('background/milieu.png')
backgroundCenterSurfaceOne = pygame.transform.scale(backgroundCenterSurface, DEFAULT_IMAGE_SIZE)
backgroundCenterSurfaceTwo = pygame.transform.rotate(backgroundCenterSurfaceOne,90)
backgroundCenterSurfaceTree = pygame.transform.rotate(backgroundCenterSurfaceOne,180)
backgroundCenterSurfaceFour = pygame.transform.rotate(backgroundCenterSurfaceOne,270)

backgroundRightSurface = pygame.image.load('background/cotedroit.png')
backgroundRightSurface = pygame.transform.scale(backgroundRightSurface, DEFAULT_IMAGE_SIZE)


# Plateforms & Resizing
plateformOneLeftSurface = pygame.image.load('platforms/plateformgauche.png')
plateformOneLeftSurface = pygame.transform.scale(plateformOneLeftSurface, DEFAULT_IMAGE_SIZE)

plateformOneCenterSurface = pygame.image.load('platforms/plateformmilieu.png')
plateformOneCenterSurface = pygame.transform.scale(plateformOneCenterSurface, DEFAULT_IMAGE_SIZE)

plateformOneRightSurface = pygame.image.load('platforms/plateformdroit.png')
plateformOneRightSurface = pygame.transform.scale(plateformOneRightSurface, DEFAULT_IMAGE_SIZE)

plateformTwoLeftSurface = pygame.image.load('platforms/plateform2gauche.png')
plateformTwoLeftSurface = pygame.transform.scale(plateformTwoLeftSurface, DEFAULT_IMAGE_SIZE)

plateformTwoCenterSurface = pygame.image.load('platforms/plateform2milieu.png')
plateformTwoCenterSurface = pygame.transform.scale(plateformTwoCenterSurface, DEFAULT_IMAGE_SIZE)

plateformTwoRightSurface = pygame.image.load('platforms/plateform2droit.png')
plateformTwoRightSurface = pygame.transform.scale(plateformTwoRightSurface, DEFAULT_IMAGE_SIZE)


# Character & Resizing
characterSurface = pygame.image.load('character/char1.png')
characterSurface = pygame.transform.scale(characterSurface, DEFAULT_IMAGE_SIZE)


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

    for i in range(0,screenWidth,64):
        for j in range(0,screenHeight,64):
            if i == 0:
                screen.blit(backgroundLeftSurface,(i,j))
            elif i == screenWidth-64:
                screen.blit(backgroundRightSurface,(i,j))
            else :
                screen.blit(backgroundCenterSurfaceOne,(i,j))#choice([backgroundCenterSurfaceOne, backgroundCenterSurfaceTwo, backgroundCenterSurfaceTree, backgroundCenterSurfaceFour])
    pygame.display.update()
    clock.tick(60)