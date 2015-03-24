
__author__ = 'clairerehfuss'


import pygame, random
from pygame.locals import *
#from Game import *

def Settings():
    click_Sound = pygame.mixer.Sound('click.wav')
    screen = pygame.display.set_mode([700, 530])
    background = pygame.image.load("SettingsScreen.png").convert()
    dragon_choice = "orange"
    sound_choice = 1
    #The button class, simply puts it on the screen

    class Button(pygame.sprite.Sprite):

        def __init__(self, location, size):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, size)
            
    redDragBtn = Button((50, 113), (120, 105))

    orangeDragBtn = Button((205,115), (120, 105))

    bandgDragBtn = Button((355, 116), (120, 105))

    blkDragBtn = Button((524,118), (120, 105))
    
    onBtn = Button((261,315), (85, 70))
    offBtn = Button((353,313), (85, 70))
    backBtn = Button((490,446), (200, 75))
    state = 0

    while state != 1:
        screen.blit(background, [0,0])
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and redDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "red"
            if(sound_choice==1):
                click_Sound.play()   
                      
        if pygame.mouse.get_pressed()[0] and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "orange"
            if(sound_choice==1):
                click_Sound.play()
                
        if pygame.mouse.get_pressed()[0] and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "blueAndGreen"
            if(sound_choice==1):
                click_Sound.play()
                
        if pygame.mouse.get_pressed()[0] and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "black"
            if(sound_choice==1):
                click_Sound.play()
                
        if pygame.mouse.get_pressed()[0] and onBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "sound on"
            sound_choice = 1
            click_Sound.play()
            
        if pygame.mouse.get_pressed()[0] and offBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "sound off"
            sound_choice = 0
            
        if pygame.mouse.get_pressed()[0] and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
            if(sound_choice==1):
                click_Sound.play()
            state = 1

                
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            
    #returns their choice of dragon and if they want the sound on or off
    #Look at key_mapping for a better understanding
    return dragon_choice, sound_choice