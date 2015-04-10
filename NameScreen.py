__author__ = 'danielleconnolly'

import pygame, random, Game, sys, eztext
from pygame.locals import *
#from Game import *

def Name(sound_choice, dragon_choice):

    screen = pygame.display.set_mode([720, 580])
    background = pygame.image.load("NameScreenNEW.jpg").convert()
    color = pygame.image.load("color.jpg").convert()
    click_sound = pygame.mixer.Sound('click.wav')

    class Button(pygame.sprite.Sprite):

        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, (125, 55))


    playBtn = Button((275, 425))
    state = 0

    # Text input courtesy of EzText http://pygame.org/project-EzText-920-.html
    textbox = eztext.Input(maxlength=45, color=(0,0,0), x=100, y=150)

    while state != 1:
        screen.blit(color, [0, 400])
        screen.blit(background, [0,0])
        events = pygame.event.get()
        textbox.update(events)
        textbox.draw(screen)
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and playBtn.rect.collidepoint(pygame.mouse.get_pos()):
            if(sound_choice == 1):
                click_sound.play()
            Game.PlayGame(35, 370, dragon_choice, sound_choice) # Go to the actual game
            state = 1
        for event in events:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
