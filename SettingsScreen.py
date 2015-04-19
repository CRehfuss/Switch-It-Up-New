
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
        def __init__(self, color, filename, resize):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(filename).convert_alpha()
            self.image.set_colorkey(color)
            self.image = pygame.transform.scale(self.image, (130,120)) # Resize sprite 
            if(resize == 1):
                self.image = pygame.transform.scale(self.image, (85,60))
                

    #Sets all the background stuff. 
    #"color"HL is when that dragon is highlighted 1 is it's on
    #"color"On is when that dragon is selected        
    redDragBtn = Button((90, 170), (115, 110))
    redHighLight = HighlightButton((255,255,255), 'hoverbox.png', 0)
    redChosen = HighlightButton((255,255,255), 'chosenbox.png', 0)
    redHL = 0
    redOn = 0
    orangeDragBtn = Button((225, 170), (115, 105))
    orangeHighLight = HighlightButton((255,255,255), 'hoverbox.png', 0)
    orangeChosen = HighlightButton((255,255,255), 'chosenbox.png', 0)
    orangeHL = 0
    orangeOn = 0
    bandgDragBtn = Button((370, 170), (120, 105))
    bandgHighLight = HighlightButton((255,255,255), 'hoverbox.png', 0)
    bandgChosen = HighlightButton((255,255,255), 'chosenbox.png', 0)
    bandgHL = 0
    bandgOn = 0
    blkDragBtn = Button((510, 170), (120, 105))
    blkHighLight = HighlightButton((255,255,255), 'hoverbox.png', 0)
    blkChosen = HighlightButton((255,255,255), 'chosenbox.png', 0)
    blkHL = 0
    blkOn = 0
    
    onBtn = Button((345, 340), (85, 60))
    onHighLight = HighlightButton((255,255,255), 'hoverbox.png', 1)
    onChosen = HighlightButton((255,255,255), 'chosenbox.png', 1)
    onHl = 0
    onOn = 0 #I'm really sorry about this variable
    
    offBtn = Button((255, 340), (75, 60))
    offHighLight = HighlightButton((255,255,255), 'hoverbox.png', 1)
    offChosen = HighlightButton((255,255,255), 'chosenbox.png', 1)
    offHl = 0
    offOn = 0
    
    backBtn = Button((275, 425), (125, 55))
    state = 0
    screen.blit(color, [0, 400])
    screen.blit(background, [0,0])
    # pygame.display.update()

    #These set what the chosen box is originally on when you first go into the screen
    if(dragon_choice=="red"):
        screen.blit(redChosen.image, [80,165]) # RED
        # pygame.display.update()
        redOn = 1
    
    if(dragon_choice=="orange"):
        screen.blit(orangeChosen.image, [220,165]) # o
        # pygame.display.update()
        orangeOn = 1
        
    if(dragon_choice == "greenandblue"):
        screen.blit(bandgChosen.image, [365,165]) # bandg
        # pygame.display.update()
        bandgOn = 1
        
    if(dragon_choice == "black"):
        screen.blit(blkChosen.image, [505,165]) # blk
        # pygame.display.update()
        blkOn = 1
    
    if(sound_choice == 1):
        screen.blit(onChosen.image, [345, 340]) #on
        # pygame.display.update()
        onOn = 1
        offOn = 0
    if(sound_choice == 0):
        screen.blit(offChosen.image, [255, 340]) #on
        # pygame.display.update()
        offOn = 1
        onOn = 0
        

    while state != 1:
        #print "settings page"
        objectsonscreen = []
        objectsonscreen.append(background)

        for event in pygame.event.get():
            pygame.display.update()
             
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
                
            if (redHL== 0 and redDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(redHighLight)
                screen.blit(redHighLight.image, [80,165]) # RED
                redHL = 1
            if (redHL == 1 and redDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off
                redHL = 0
            if event.type == MOUSEBUTTONDOWN and redDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if (orangeOn == 1 or bandgOn == 1 or blkOn == 1):
                    objectsonscreen = [background]
                    screen.blit(background, (0,0))
                    orangeOn = 0
                    bandgOn=0
                    blkOn=0
                if(sound_choice == 1):
                    screen.blit(onChosen.image, [345,340])
                if(sound_choice == 0):
                    screen.blit(offChosen.image,[255, 340])                   
                dragon_choice = "red"
                redOn = 1
                screen.blit(redChosen.image, [80,165]) # RED
                # pygame.display.update()
                if(sound_choice==1):
                    click_Sound.play()
                    
            if (orangeHL == 0 and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(orangeHighLight)
                screen.blit(orangeHighLight.image, [220, 165]) # ORANGE
                # pygame.display.update()
                orangeHL = 1
            if (orangeHL == 1 and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off
                orangeHL = 0  
            if event.type == MOUSEBUTTONDOWN and orangeDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if (redOn == 1 or bandgOn == 1 or blkOn == 1):
                    objectsonscreen = [background]
                    screen.blit(background, (0,0))
                    redOn = 0
                    bandgOn = 0
                    blkOn = 0

                if(sound_choice == 1):
                    screen.blit(onChosen.image, [345,340])
                if(sound_choice == 0):
                    screen.blit(offChosen.image,[255, 340])                    
                dragon_choice = "orange"
                screen.blit(orangeChosen.image, [220,165]) # RED
                # pygame.display.update()
                orangeOn = 1
                if(sound_choice==1):
                    click_Sound.play()
            
            #Blue and green dragon
            if (bandgHL == 0 and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(bandgHighLight)
                screen.blit(bandgHighLight.image, [365, 165]) # BLUE/GREEN
                # pygame.display.update()
                bandgHL = 1
            if (bandgHL == 1 and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off
                bandgHL = 0    
            if event.type == MOUSEBUTTONDOWN and bandgDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if (orangeOn == 1 or redOn == 1 or blkOn == 1):
                    objectsonscreen = [background]
                    screen.blit(background, (0,0))
                    orangeOn = 0
                    redOn = 0
                    blkOn = 0
                if(sound_choice == 1):
                    screen.blit(onChosen.image, [345,340])
                if(sound_choice == 0):
                    screen.blit(offChosen.image,[255, 340])
                dragon_choice = "greenandblue"
                screen.blit(bandgChosen.image, [365,165]) # RED
                # pygame.display.update()
                bandgOn = 1
                if(sound_choice==1):
                    click_Sound.play()
                    
            #BLACK dragon
            if (blkHL == 0 and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos())):
                screen.blit(blkHighLight.image, [505,165]) # BLACK
                # pygame.display.update()
                blkHL = 1
            if (blkHL == 1 and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off
                blkHL = 0
            if event.type == MOUSEBUTTONDOWN and blkDragBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if (orangeOn == 1 or bandgOn == 1 or redOn == 1):
                    objectsonscreen = [background]
                    screen.blit(background, (0,0))
                    orangeOn = 0
                    bandgOn= 0
                    redOn = 0
                if(sound_choice == 1):
                    screen.blit(onChosen.image, [345,340])
                if(sound_choice == 0):
                    screen.blit(offChosen.image,[255, 340])
                dragon_choice = "black"
                blkOn = 1
                screen.blit(blkChosen.image, [505,165]) # RED
                # pygame.display.update()
                if(sound_choice==1):
                    click_Sound.play()
                    
            #ON button
            if (onHl == 0 and onBtn.rect.collidepoint(pygame.mouse.get_pos())):
                objectsonscreen.append(onHighLight)
                screen.blit(onHighLight.image, [345, 340]) # on highlight
                # pygame.display.update()
                onHl = 1
            if (onHl == 1 and onBtn.rect.collidepoint(pygame.mouse.get_pos())==False):
                objectsonscreen = [background]
                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off  
                #pygame.display.update()
                onHl = 0
            if event.type == MOUSEBUTTONDOWN and onBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if(offOn == 1):
                    offOn = 0
                    screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                screen.blit(onChosen.image, [345,340]) # On highlight
                onOn = 1
                # pygame.display.update()
                sound_choice = 1
                click_Sound.play()
            
            #SOUND OFF
            if (offHl == 0 and offBtn.rect.collidepoint(pygame.mouse.get_pos())):
                screen.blit(offHighLight.image, [255, 340]) # BLUE/GREEN
                # pygame.display.update()
                offHl = 1
                
            if (offHl == 1 and offBtn.rect.collidepoint(pygame.mouse.get_pos())==False):

                screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                    # pygame.display.update()
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                    # pygame.display.update()
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                    # pygame.display.update()
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                    # pygame.display.update()
                if(onOn == 1):
                    screen.blit(onChosen.image, [345,340]) #sound on
                    # pygame.display.update()
                if(offOn == 1):
                    screen.blit(offChosen.image, [255, 340]) #sound off
                    # pygame.display.update()
                offHl = 0
                
            if event.type == MOUSEBUTTONDOWN and offBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if(onOn == 1):
                    onOn = 0
                    screen.blit(background, (0,0))
                if(redOn==1):
                    screen.blit(redChosen.image, [80,165]) # RED
                if(orangeOn ==1):
                    screen.blit(orangeChosen.image, [220,165]) # o
                if(bandgOn == 1):
                    screen.blit(bandgChosen.image, [365,165]) # bandg
                if(blkOn ==1):
                    screen.blit(blkChosen.image, [505,165]) # blk
                screen.blit(offChosen.image, [255,340]) # Off chosen
                offOn = 1
                # pygame.display.update()
                sound_choice = 0
  
                
            if event.type == MOUSEBUTTONDOWN and backBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if(sound_choice==1):
                    click_Sound.play()
                state = 1
            
    #returns their choice of dragon and if they want the sound on or off
    #Look at key_mapping for a better understanding
    return dragon_choice, sound_choice