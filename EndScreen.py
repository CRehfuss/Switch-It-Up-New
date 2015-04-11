__author__ = 'danielleconnolly'

import pygame, random, Game
from pygame.locals import *
#from Game import *

screen = pygame.display.set_mode([720, 580])
background = pygame.image.load("winNEW.jpg").convert()
color = pygame.image.load("color.jpg").convert()


class Button(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(location, (200, 80))

def YouWin(dragon_choice, sound_choice):

    replayBtn = Button((135, 240))
    quitBtn = Button((385, 240))
    state = 0
    click_sound = pygame.mixer.Sound('click.wav')
    while state != 1:
        screen.blit(color, [0, 400])
        screen.blit(background, [0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            elif event.type == MOUSEBUTTONDOWN and replayBtn.rect.collidepoint(pygame.mouse.get_pos()):
                print "play again button"
                state = 1
                if(sound_choice==1):
                    click_sound.play()
                Game.PlayGame(35, 370, dragon_choice, sound_choice)
            elif event.type == MOUSEBUTTONDOWN and quitBtn.rect.collidepoint(pygame.mouse.get_pos()):
                print "quit button"
                state = 1
                if(sound_choice==1):
                    click_sound.play()


