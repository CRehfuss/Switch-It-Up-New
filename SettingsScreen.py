
__author__ = 'clairerehfuss'


import pygame, random
from pygame.locals import *
#from Game import *

def Settings(dragon_choice,sound_choice):
    print "settings called"
    click_Sound = pygame.mixer.Sound('click.wav')
    screen = pygame.display.set_mode([720, 580])
    background = pygame.image.load("settingsNEW.jpg").convert()
    color = pygame.image.load("color.jpg").convert()

    #The button class, simply puts it on the screen

    class Button(pygame.sprite.Sprite):

        def __init__(self, location, size):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, size)
            
    redDragBtn = Button((90, 170), (115, 110))
    orangeDragBtn = Button((225, 170), (115, 105))
    bandgDragBtn = Button((370, 170), (120, 105))
    blkDragBtn = Button((510, 170), (120, 105))
    
    onBtn = Button((345, 340), (85, 60))
    offBtn = Button((255, 340), (75, 60))
    backBtn = Button((275, 425), (125, 55))
    state = 0

    while state != 1:
        print "settings page"
        screen.blit(color, [0, 400])
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
            dragon_choice = "greenandblue"
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