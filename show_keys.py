import pygame, random, Game
from pygame.locals import *
from Game import *

def showKeys(avatar, screens):



    upstring = "../Resources/keys/" + avatar.upkey + ".jpg"
    downstring = "../Resources/keys/" + avatar.downkey + ".jpg"
    leftstring = "../Resources/keys/" + avatar.leftkey + ".jpg"
    rightstring = "../Resources/keys/" + avatar.rightkey + ".jpg"


    screens.blit(upstring, (10,0))
    screens.blit(downstring, (10, 20))
    screens.blit(leftstring, (0, 10))
    screens.blit(rightstring, (20,10))

