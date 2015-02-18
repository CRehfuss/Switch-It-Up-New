__author__ = 'danielleconnolly'

import pygame, random, Maze
from pygame.locals import *
#from Game import *

screen = pygame.display.set_mode([700, 500])
background = pygame.image.load("titlescreen.jpg").convert()

class Button(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(location, (180, 110))


startBtn = Button((55, 275))
state = 0

while state != 1:
    screen.blit(background, [0,0])
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] and startBtn.rect.collidepoint(pygame.mouse.get_pos()):
        print "clicked the start button"
        Maze.WallScreen()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
