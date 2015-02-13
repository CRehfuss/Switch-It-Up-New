#Switch it Up
#Main file


import pygame, random

from pygame.locals import *
from Alpha_Release import key_mapping


pygame.init()

screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption("Switch It Up")

x_Dragon = 0
y_Dragon = 0


#Animates images
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
    
    def __init__(self, color, width, height, filename, location): #should location be a parameter? - Tyler
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.all_images = AnimationImages(width, height, filename)
        
        # delay is time between animation frames
        # last_update saves the time the animation was last updated     
        self.delay = 100
        self.last_update = 0
        
         # frame is the array location in images
        self.frame = 0
      #  self.location = location[0]

        # sets the animations current image
        self.image = self.all_images[self.frame]
        self.image.set_colorkey(color) 
        self.rect = self.image.get_rect()       

        # position the image
        #self.Reset(self)
       
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        # sets the lives to three
        self.lives = 3

        #initialize players up down left right (Do I have to do this, Let's see)
        self.upkey, self.downkey, self.leftkey, self.rightkey = key_mapping.getKeys(0)
    
    def getNumLives(self):
        return self.lives
    
    #Checks if the dragon is colliding with the wall
    def getCollision(self, wall2):
        global x_Dragon
        global y_Dragon
        
        if pygame.sprite.collide_rect(self, block2):
            
            x_Dragon = random.randrange(700 - self.rect.width)
            
            y_Dragon = random.randrange(500 - self.rect.height)


    def moveDown(self):
        global y_Dragon
        y_Dragon -= 2
    
    def moveUp(self):
        global y_Dragon
        y_Dragon += 2
    
    def moveLeft(self):
        global x_Dragon
        x_Dragon -= 2
        
    def moveRight(self):
        global x_Dragon
        x_Dragon += 2
        
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



state = 0
while state != 1:
    
    #Just a white screen
    screen.fill([255,255,255])


    # create the dragon image
    dragon = Player((255,255,255), 128, 114, "../Dragons.png", (x_Dragon, y_Dragon))


    keypressed = pygame.key.get_pressed()

    if keypressed[dragon.upkey]:
        dragon.moveup()
    if keypressed[dragon.downkey]:
        dragon.movedown()
    if keypressed[dragon.leftkey]:
        dragon.moveleft()
    if keypressed[dragon.rightkey]:
        dragon.moveright()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1
        
        
        
        
        
        
        
