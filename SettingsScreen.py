
__author__ = 'clairerehfuss'


import pygame, random
from pygame.locals import *
#from Game import *

def Settings():
    
    screen = pygame.display.set_mode([700, 520])
    background = pygame.image.load("settingsscreen.jpg").convert()
    dragon_choice = "orange"
    sound_choice = 0
    #The button class, simply puts it on the screen
    class DragonButton(pygame.sprite.Sprite):

            def __init__(self, location):
                pygame.sprite.Sprite.__init__(self)
                self.rect = Rect(location, (120, 110))
    
    class BackButton(pygame.sprite.Sprite):

            def __init__(self, location):
                pygame.sprite.Sprite.__init__(self)
                self.rect = Rect(location, (200, 78))

    class SoundButton(pygame.sprite.Sprite):

            def __init__(self, location):
                pygame.sprite.Sprite.__init__(self)
                self.rect = Rect(location, (87, 72))
            
    dragon_choice = "orange"
    redDragBtn = DragonButton((63, 115))
    print "redDragon"
    orangeDragBtn = DragonButton((202,113))
    print "orangeDragon"
    bandgDragBtn = DragonButton((335, 110))
    print "blue and green Dragon"
    blkDragBtn = DragonButton((508,115))
    print "BLACK Dragaggon"
    
    onBtn = SoundButton((251,314))
    offBtn = SoundButton((362,315))
    backBtn = BackButton((472,395))
    state = 0

    while state != 1:
        screen.blit(background, [0,0])
        pygame.display.update()
        if pygame.mouse.get_pressed()[0] and redDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "red"
            print "red chosen"
        if pygame.mouse.get_pressed()[0] and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "orange"
            print "orange chosen"
        if pygame.mouse.get_pressed()[0] and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "blueAndGreen"
            print "blue and green chosen"
        if pygame.mouse.get_pressed()[0] and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
            dragon_choice = "black"
            print "black chosen"
        if pygame.mouse.get_pressed()[0] and onBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "sound on"
            sound_choice = 1
        if pygame.mouse.get_pressed()[0] and offBtn.rect.collidepoint(pygame.mouse.get_pos()):
            print "sound off"
            sound_choice = 0
        if pygame.mouse.get_pressed()[0] and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
            state = 1
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            
        
        
        
    #returns their choice of dragon and if they want the sound on or off
    #Look at key_mapping for a better understanding
    return dragon_choice, sound_choice