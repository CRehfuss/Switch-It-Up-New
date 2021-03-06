__author__ = 'danielleconnolly'


import pygame, random
from pygame.locals import *
#from Game import *

def Instructions(sound_choice):

    screen = pygame.display.set_mode([720, 580])
    background = pygame.image.load("howtoplayNEW.jpg").convert()
    color = pygame.image.load("color.jpg").convert()
    click_sound = pygame.mixer.Sound('click.wav')

    class Button(pygame.sprite.Sprite):

        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, (125, 55))


    backBtn = Button((275, 425))
    state = 0

    while state != 1:
        screen.blit(color, [0, 400])
        screen.blit(background, [0,0])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            elif event.type == MOUSEBUTTONDOWN and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if(sound_choice == 1):
                    click_sound.play()
                state = 1

