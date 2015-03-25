__author__ = 'danielleconnolly'


import pygame, random
from pygame.locals import *
#from Game import *

def Instructions(sound_choice):

    screen = pygame.display.set_mode([720, 540])
    background = pygame.image.load("howtoplayNEW.jpg").convert()
    click_sound = pygame.mixer.Sound('click.wav')

    class Button(pygame.sprite.Sprite):

        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, (125, 55))


    backBtn = Button((275, 425))
    state = 0

    while state != 1:
        screen.blit(background, [0,0])
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
            if(sound_choice == 1):
                click_sound.play()
            state = 1
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1

