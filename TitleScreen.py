__author__ = 'danielleconnolly'

import pygame, random, InstructionScreen, Game, key_mapping, SettingsScreen
from pygame.locals import *
#from Game import *

screen = pygame.display.set_mode([700, 530])
background = pygame.image.load("titlescreen.jpg").convert()

class Button(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(location, (180, 110))



startBtn = Button((55, 275))
instructBtn = Button((260, 275))
settingsBtn = Button((455, 275))
state = 0

dragon_choice = "orange"
sound_choice = 1 
click_sound = pygame.mixer.Sound('click.wav')
while state != 1:
    screen.blit(background, [0,0])
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] and startBtn.rect.collidepoint(pygame.mouse.get_pos()):
        print "start button"
        if (sound_choice ==1):
            click_sound.play()
            print "click"
        Game.PlayGame(35, 370, dragon_choice, sound_choice)
        state = 1
    elif pygame.mouse.get_pressed()[0] and instructBtn.rect.collidepoint(pygame.mouse.get_pos()):
        print "instruction button"
        if(sound_choice ==1):
            click_sound.play()
            print "click"
        InstructionScreen.Instructions(sound_choice)
    elif pygame.mouse.get_pressed()[0] and settingsBtn.rect.collidepoint(pygame.mouse.get_pos()):
        print "settings button"
        if(sound_choice==1):
            click_sound.play()
        dragon_choice, sound_choice = SettingsScreen.Settings()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
