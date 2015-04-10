__author__ = 'danielleconnolly'

import pygame, random, InstructionScreen, key_mapping, SettingsScreen, AboutScreen, Game
from pygame.locals import *


screen = pygame.display.set_mode([720, 580])
background = pygame.image.load("titlescreenNEW.jpg").convert()
color = pygame.image.load("color.jpg").convert()

class Button(pygame.sprite.Sprite):

    def __init__(self, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(location, size)



pygame.mixer.init(44100, -16, 2, 2048)

startBtn = Button((255, 195), (200, 80))
instructBtn = Button((280, 300), (155, 60))
settingsBtn = Button((95, 300), (155, 60))
aboutBtn = Button((460, 300), (155, 60))
state = 0

dragon_choice = "orange"
sound_choice = 1#TYLER CHANGED THIS TO 0, It's annoying af- Tyler #NO WHY STOP
pygame.mixer.init(44100, -16, 2, 2048)
click_sound = pygame.mixer.Sound('click.wav')
while state != 1:
    screen.blit(color, [0,400])
    screen.blit(background, [0,0])
    pygame.display.update()
    if pygame.mouse.get_pressed()[0] and startBtn.rect.collidepoint(pygame.mouse.get_pos()):
        #print "start button"
        if (sound_choice == 1):
            click_sound.play()
        Game.PlayGame(35, 370, dragon_choice, sound_choice)
        state = 1
    if pygame.mouse.get_pressed()[0] and instructBtn.rect.collidepoint(pygame.mouse.get_pos()):
        #print "instruction button"
        if(sound_choice == 1):
            click_sound.play()
        InstructionScreen.Instructions(sound_choice)
    if pygame.mouse.get_pressed()[0] and aboutBtn.rect.collidepoint(pygame.mouse.get_pos()):
        #print "about button"
        if(sound_choice == 1):
            click_sound.play()
        AboutScreen.About(sound_choice)
    if pygame.mouse.get_pressed()[0] and settingsBtn.rect.collidepoint(pygame.mouse.get_pos()):
        #print "settings button"
        if(sound_choice==1):
            click_sound.play()
        dragon_choice, sound_choice = SettingsScreen.Settings(dragon_choice, sound_choice)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1

