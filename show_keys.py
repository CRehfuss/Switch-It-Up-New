import pygame, random, Game
from pygame.locals import *
from Game import *

def showKeys(dragon, screen):

    upstring = "../Resources/keys/" + dragon.upkey + ".jpg"
    downstring = "../Resources/keys/" + dragon.downkey + ".jpg"
    leftstring = "../Resources/keys/" + dragon.leftkey + ".jpg"
    rightkey = "../Resources/keys/" + dragon.rightkey + ".jpg"

    screen.blit(upstring, (0,0))
