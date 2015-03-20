__author__ = 'danielleconnolly'


import pygame, random
from pygame.locals import *
#from Game import *

def Instructions():

    screen = pygame.display.set_mode([700, 520])
    background = pygame.image.load("instructionscreen.jpg").convert()

    class Button(pygame.sprite.Sprite):

        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, (195, 95))


    backBtn = Button((410, 345))
    state = 0

    while state != 1:
        screen.blit(background, [0,0])
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
            state = 1
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1

