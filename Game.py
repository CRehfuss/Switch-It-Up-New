#Main file


import random, key_mapping
import pygame
from pygame.locals import *




pygame.init()

screenwidth = 700
screenheight = 500

screen = pygame.display.set_mode([screenwidth,screenheight])
pygame.display.set_caption("Switch It Up")

x_Dragon = 35
y_Dragon = 350


#Animates images from discussion 4
def AnimationImages(width, height, filename): #defining a function have to do it before
    # images array will be filled with each frame of an animation
    images = []
    
    fullImage = pygame.image.load(filename).convert_alpha()
    fullWidth, fullHeight = fullImage.get_size()
    
    for i in xrange(int(fullWidth/width)):
        images.append(fullImage.subsurface((i*width, 0, width ,height)))
        
    return images


def showKeys(avatar, screens):


    keylist = avatar.upkey, avatar.downkey, avatar.leftkey, avatar.rightkey
    keystr = []
    for key in keylist:

        if(key == K_UP):
            keystr.append("up")
        if(key == K_DOWN):
            keystr.append("down")
        if(key == K_LEFT):
            keystr.append("left")
        if(key == K_RIGHT):
            keystr.append("right")


    upstring = "Resources/keys/" + keystr[0] + ".jpg"
    downstring = "Resources/keys/" + keystr[1] + ".jpg"
    leftstring = "Resources/keys/" + keystr[2] + ".jpg"
    rightstring = "Resources/keys/" + keystr[3] + ".jpg"


    screens.blit(pygame.image.load(upstring).convert_alpha(), (20, 0))
    screens.blit(pygame.image.load(downstring).convert_alpha(), (20, 40))
    screens.blit(pygame.image.load(leftstring).convert_alpha(), (0, 20))
    screens.blit(pygame.image.load(rightstring).convert_alpha(), (40, 20))




#The Implementation of Player class should follow
class Player(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, filename, location, difficulty):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        
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
    def getCollision(self, wall_1, direction):
        global x_Dragon
        global y_Dragon
        
        if pygame.sprite.collide_rect(self, wall_1):
            if(direction=="up"):
                y_Dragon-=1
            if(direction == "down"):
                y_Dragon += 1
            if(direction == "right"):
                x_Dragon -= 1
            if(direction == "left"):
                x_Dragon += 1
                
    def moveDown(self):
        global y_Dragon
        y_Dragon += .35
    
    def moveUp(self):
        global y_Dragon
        y_Dragon -= .35
    
    def moveLeft(self):
        global x_Dragon
        x_Dragon -= .35
        
    def moveRight(self):
        global x_Dragon
        x_Dragon += .35

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
        

class Walls(pygame.sprite.Sprite):
    def __init__(self, x_wall, y_wall, x_width, y_length):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([x_width, y_length])
        self.image.fill((225, 29, 94))
        self.rect = self.image.get_rect()        
        self.rect.x = x_wall
        self.rect.y = y_wall
mazes = []
# implementation inspired by simpson college CS

wall_list_1 = pygame.sprite.Group()
wall_1 = [[30, 30, 5, 410], #left
        [30, 440, 640, 5], #bottom
        [30, 30, 640, 5], #top
        [670, 30, 5, 415 ], #right
        [30, 330, 570, 5],
        [266, 387, 300, 5],
        [600, 85, 5, 250],
        [95, 82, 510,5],
        [95, 82, 5, 200],
        [95, 280, 440, 5],
        [530, 135, 5, 150],
        [160, 135, 370, 5],
        [160, 135, 5, 70],
        [160, 200, 300, 5]
        # end of maze at 194,172~
        ]
        # add each part of wall to a list
for var in wall_1:
    wall = Walls(var[0], var[1], var[2], var[3])
    wall_list_1.add(wall)
mazes.append(wall_list_1)
wall_list_2 = pygame.sprite.Group()
wall_2 = [[30, 30, 5, 410], #left
        [30, 440, 640, 5], #bottom
        [30, 30, 640, 5], #top
        [670, 30, 5, 415 ], #right
        [30, 385, 490, 5],
        [600, 385, 70, 5],
        [30, 385, 490, 5],
        [515, 215, 5, 175],
        [515, 300, 80, 5],
        [250, 215, 270, 5],
        [385, 120, 5, 100],
        [590, 120, 5, 100],
        [515, 120, 80, 5],
        [515, 30, 5, 95],
        [150, 120, 100, 5],
        [150, 120, 5, 180],
        [150, 300, 300, 5],
        [30, 120, 60, 5],
        [90, 120, 5, 184],
        [90, 300, 60, 5],
        #end maze at 64,150

        ]
        # add each part of wall to a list
for var in wall_2:
    wall = Walls(var[0], var[1], var[2], var[3])
    wall_list_2.add(wall)
mazes.append(wall_list_2)
wall_list_3 = pygame.sprite.Group()
wall_3 = [[30, 30, 5, 410], #left
        [30, 440, 640, 5], #bottom
        [30, 30, 640, 5], #top
        [670, 30, 5, 415 ], #right
        [90, 385, 5, 60],
        [30, 330, 130, 5],
        [160, 330, 5, 50],
        [245, 90, 5, 350],
        [95, 90, 150, 5],
        [95, 90, 5, 150],
        [95, 240, 60, 5],
        [350, 90, 5, 280],
        [350, 90, 225, 5],
        [350, 370, 230, 5],
        [575, 90, 5, 68],
        [575, 310, 5, 60],
        [300, 90, 5, 284],
        [420, 145, 5, 165],
        [420, 240, 255, 5],
        [420, 305, 160, 5],
        [420, 190, 90, 5],
        #end at 551,343
        ]
        # add each part of wall to a list
for var in wall_3:
    wall = Walls(var[0], var[1], var[2], var[3])
    wall_list_3.add(wall)
mazes.append(wall_list_3)

dragon = Player((255,255,255), 72, 64, "Resources/Dragons.png", [x_Dragon, y_Dragon], 0)
screen.blit(dragon.image, dragon)


room = 0
GameOver = 0
state = 0
while state != 1:
    
    #Just a white screen
    screen.fill([255,255,255])
     # create the dragon image
    showKeys(dragon, screen)
    dragon.rect.x = x_Dragon
    dragon.rect.y = y_Dragon

    timer = pygame.time.get_ticks()  
    
    dragon.updateAnimation(timer)

    mazes[room].draw(screen)

    pygame.display.update()
    badkeycount = 0

    keypressed = pygame.key.get_pressed()

#This should work once we put the wall class in
    if keypressed[dragon.upkey]:
        dragon.moveUp()
        #for objects in mazes[room]:
         #   dragon.getCollision(objects, "up")
    if keypressed[dragon.downkey]:
        dragon.moveDown()
        #for objects in mazes[room]:
        #    dragon.getCollision(objects, "down")
    if keypressed[dragon.leftkey]:
        dragon.moveLeft()
        #for objects in mazes[room]:
          #  dragon.getCollision(objects, "left")
    if keypressed[dragon.rightkey]:
        dragon.moveRight()
        #for objects in mazes[room]:
         #   dragon.getCollision(objects, "right")


    #Stops the Player from running off the screen
    if x_Dragon > screenwidth - dragon.width:
        x_Dragon = screenwidth - dragon.width

    if x_Dragon < 0:
        x_Dragon = 0

    if y_Dragon > screenheight - dragon.height:
        y_Dragon = screenheight - dragon.height

    if y_Dragon < 0:
        y_Dragon = 0


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            state = 1

        if event.type == KEYDOWN and (event.key != dragon.upkey):
                badkeycount += 1
                if badkeycount > 20:

                    showKeys(dragon, screen)

        if event.type == KEYDOWN and event.key != dragon.downkey:
                badkeycount += 1
                if badkeycount > 20:

                 showKeys(dragon, screen)

        if event.type == KEYDOWN and event.key != dragon.leftkey:
                badkeycount += 1
                if badkeycount > 20:

                 showKeys(dragon, screen)

        if event.type == KEYDOWN and event.key != dragon.rightkey:
                badkeycount += 1

                if badkeycount > 20:

                  showKeys(dragon, screen)
