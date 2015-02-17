#Switch it Up
#Main file


import random, key_mapping, show_keys
import pygame
from pygame.locals import *
from show_keys import *



pygame.init()

screen = pygame.display.set_mode([700,500])
pygame.display.set_caption("Switch It Up")

x_Dragon = 350
y_Dragon = 250


#Animates images from discussion 4
def AnimationImages(width, height, filename): #defining a function have to do it before
    # images array will be filled with each frame of an animation
    images = []
    
    fullImage = pygame.image.load(filename).convert_alpha()
    fullWidth, fullHeight = fullImage.get_size()
    
    for i in xrange(int(fullWidth/width)):
        images.append(fullImage.subsurface((i*width, 0, width ,height)))
        
    return images


#The Implementation of Player class should follow
class Player(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, filename, location, difficulty):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.all_images = AnimationImages(width,height,filename)
        
        # delay is time between animation frames
        # last_update saves the time the animation was last updated     
        self.delay = 100
        self.last_update = 0
        
         # frame is the array location in images
        self.frame = 0
        self.location = location
        
        # sets the animations current image
        self.image = self.all_images[self.frame]
        self.image.set_colorkey(color) 
        self.rect = self.image.get_rect()       

        # position the image
        #self.Reset(self)
       
        self.rect.x = 0
        self.rect.y = 0

        #setting the difficulty of key mapping for this avatar
        self.difficulty = difficulty


        self.upkey, self.downkey, self.leftkey, self.rightkey = key_mapping.getKeys(difficulty)
        
        # sets the lives to three
        self.lives = 3
    
    def getNumLives(self):
        return self.lives
    
    #Checks if the dragon is colliding with the wall
    def getCollision(self, wall2):
        global x_Dragon
        global y_Dragon
        
        if pygame.sprite.collide_rect(self, wall2):
            
            x_Dragon = random.randrange(700 - self.rect.width)
            
            y_Dragon = random.randrange(500 - self.rect.height)
            
    def moveDown(self):
        global y_Dragon
        y_Dragon += .5
    
    def moveUp(self):
        global y_Dragon
        y_Dragon -= .5
    
    def moveLeft(self):
        global x_Dragon
        x_Dragon -= .5
        
    def moveRight(self):
        global x_Dragon
        x_Dragon += .5

     #Fourth discussion   
    def updateAnimation (self, totalTime):
        
        # checks if enough time has passed to change the image
        if totalTime - self.last_update > self.delay:
            self.frame += 1
            
            # checks if the new image is greater than the number of images
            # starts image cycle over if true
            if self.frame >= len(self.all_images): 
                self.frame = 0
                
            # updates current animation image
            self.image = self.all_images[self.frame]
            
            # changes the last update time
            self.last_update = totalTime
        
        #draws animation changes to the screen
        screen.blit(self.image, self)
        

dragon = Player((255,255,255), 128, 114, "Dragons.png", [x_Dragon, y_Dragon], 0)
screen.blit(dragon.image, dragon)



GameOver = 0
state = 0
while state != 1:
    
    #Just a white screen
    screen.fill([255,255,255])
     # create the dragon image

    dragon.rect.x = x_Dragon
    dragon.rect.y = y_Dragon

    timer = pygame.time.get_ticks()  
    
    dragon.updateAnimation(timer)



    pygame.display.update()
    badkeycount = 0

    keypressed = pygame.key.get_pressed()

    if keypressed[dragon.upkey]:
        dragon.moveUp()
    if keypressed[dragon.downkey]:
        dragon.moveDown()
    if keypressed[dragon.leftkey]:
        dragon.moveLeft()
    if keypressed[dragon.rightkey]:
        dragon.moveRight()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1

        if event.type == KEYDOWN and (event.key != dragon.upkey):
                badkeycount += 1
        if event.type == KEYDOWN and event.key != dragon.downkey:
                badkeycount += 1
        if event.type == KEYDOWN and event.key != dragon.leftkey:
                badkeycount += 1
        if event.type == KEYDOWN and event.key != dragon.rightkey:
                badkeycount += 1
        if badkeycount > 20:
            #prompt the correct keys (How is yet to be established)
             showKeys(dragon)
