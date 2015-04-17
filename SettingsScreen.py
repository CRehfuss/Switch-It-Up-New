
__author__ = 'clairerehfuss'


import pygame, random
from pygame.locals import *
#from Game import *

def Settings(dragon_choice,sound_choice):
    #print "settings called"
    click_Sound = pygame.mixer.Sound('click.wav')
    screen = pygame.display.set_mode([720, 580])
    background = pygame.image.load("settingsNEW.jpg").convert()
    color = pygame.image.load("color.jpg").convert()

    #The button class, simply puts it on the screen

    class Button(pygame.sprite.Sprite):

        def __init__(self, location, size):
            pygame.sprite.Sprite.__init__(self)
            self.rect = Rect(location, size)
            
    class HighlightButton(pygame.sprite.Sprite):
        def __init__(self, color, filename):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(filename).convert_alpha()
            self.image.set_colorkey(color) 

            
    redDragBtn = Button((90, 170), (115, 110))
    redHighLight = HighlightButton((255,255,255), 'hoverbox.png')
    redHL = 0
    orangeDragBtn = Button((225, 170), (115, 105))
    orangeHighLight = HighlightButton((255,255,255), 'hoverbox.png')
    orangeHL = 0
    bandgDragBtn = Button((370, 170), (120, 105))
    bandgHighLight = HighlightButton((255,255,255), 'hoverbox.png')
    bandgHL = 0
    blkDragBtn = Button((510, 170), (120, 105))
    blkHighLight = HighlightButton((255,255,255), 'hoverbox.png')
    blkHL = 0
    
    onBtn = Button((345, 340), (85, 60))
    offBtn = Button((255, 340), (75, 60))
    backBtn = Button((275, 425), (125, 55))
    state = 0
    screen.blit(color, [0, 400])
    screen.blit(background, [0,0])
    pygame.display.update()

    while state != 1:
        #print "settings page"
        objectsonscreen = []
        objectsonscreen.append(background)

        for event in pygame.event.get():
            
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
                
            if (redHL== 0 and redDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(redHighLight)
                screen.blit(redHighLight.image, [90,170])
                pygame.display.update()
                redHL = 1
                print "OVER RED"
            if (redHL == 1 and redDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                print "UNBLIT R"
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                pygame.display.update()
                redHL = 0
            if event.type == MOUSEBUTTONDOWN and redDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                dragon_choice = "red"
                if(sound_choice==1):
                    click_Sound.play()
                    
            if (orangeHL == 0 and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(orangeHighLight)
                screen.blit(orangeHighLight.image, [225, 170])
                pygame.display.update()
                orangeHL = 1
            if (orangeHL == 1 and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                print "UNBLIT O"
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                pygame.display.update()
                orangeHL = 0  
            if event.type == MOUSEBUTTONDOWN and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                dragon_choice = "orange"
                if(sound_choice==1):
                    click_Sound.play()
            
            if (bandgHL == 0 and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(bandgHighLight)
                screen.blit(bandgHighLight.image, [370, 170])
                pygame.display.update()
                bandgHL = 1
            if (bandgHL == 1 and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                print "UNBLIT bandg"
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                pygame.display.update()
                bandgHL = 0    
            if event.type == MOUSEBUTTONDOWN and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                dragon_choice = "greenandblue"
                if(sound_choice==1):
                    click_Sound.play()
                    
            if (blkHL == 0 and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(blkHighLight)
                screen.blit(blkHighLight.image, [510,170])
                pygame.display.update()
                blkHL = 1
            if (blkHL == 1 and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                print "UNBLIT BLK"
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                pygame.display.update()
                blkHL = 0
            if event.type == MOUSEBUTTONDOWN and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                dragon_choice = "black"
                if(sound_choice==1):
                    click_Sound.play()
                    
            if event.type == MOUSEBUTTONDOWN and onBtn.rect.collidepoint(pygame.mouse.get_pos()):
                sound_choice = 1
                click_Sound.play()
            if event.type == MOUSEBUTTONDOWN and offBtn.rect.collidepoint(pygame.mouse.get_pos()):
                sound_choice = 0
            if event.type == MOUSEBUTTONDOWN and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if(sound_choice==1):
                    click_Sound.play()
                state = 1
            
    #returns their choice of dragon and if they want the sound on or off
    #Look at key_mapping for a better understanding
    return dragon_choice, sound_choice