__author__ = 'danielleconnolly'

import pygame, random, Game
from pygame.locals import *
#from Game import *

screen = pygame.display.set_mode([700, 530])
background = pygame.image.load("win.jpg").convert()

class Button(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(location, (200, 90))

def YouWin(dragon_choice, sound_choice):

    replayBtn = Button((115, 285))
    quitBtn = Button((365, 285))
    state = 0

    while state != 1:
        screen.blit(background, [0,0])
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and replayBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "play again button"
            state = 1
            Game.PlayGame(35, 370, dragon_choice, sound_choice)
        if pygame.mouse.get_pressed()[0] and quitBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "quit button"
            state = 1
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1


