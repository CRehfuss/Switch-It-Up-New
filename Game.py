#Main file


import random, key_mapping, EndScreen
import pygame
from pygame.locals import *




pygame.init()

screenwidth = 700
screenheight = 530

screen = pygame.display.set_mode([screenwidth,screenheight])
pygame.display.set_caption("Switch It Up")

global livesLeft
livesLeft = 3 # Number of lives starts at 3

x_Dragon = 35
y_Dragon = 370
gamespeed = 2
state = 0
coll = 0



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

    keyLocations = [[630, 465], [630, 505], [610, 485], [650, 485]] # up, down, left, right


    screens.blit(pygame.image.load(upstring).convert_alpha(), keyLocations[0])
    screens.blit(pygame.image.load(downstring).convert_alpha(), keyLocations[1])
    screens.blit(pygame.image.load(leftstring).convert_alpha(), keyLocations[2])
    screens.blit(pygame.image.load(rightstring).convert_alpha(), keyLocations[3])




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




    #tests if 3 points on the box will hit a wall depending on what direction the player wants to move
    def canMove(self, direction, maze):

        global x_Dragon
        global y_Dragon
        global gamespeed
        #check the four corners of the rect depending on which direction the player wants to move
        #returns FALSE if player cannot move in that direction
        if (direction == "up") & (isWall(maze, self.rect.x, self.rect.y - gamespeed) | isWall(maze, self.rect.x + self.width/4, self.rect.y - gamespeed) | isWall(maze, self.rect.x + self.width/2, self.rect.y -gamespeed) | isWall(maze, self.rect.x + (3/4)*self.width, self.rect.y - gamespeed) | isWall(maze, self.rect.x + self.width, self.rect.y - gamespeed)):
            return False
        if (direction == "down") & (isWall(maze, self.rect.x, self.rect.y + self.height + gamespeed) |isWall(maze, self.rect.x + self.width/4, self.rect.y + self.height + gamespeed) | isWall(maze, self.rect.x + self.width/2, self.rect.y + self.height + gamespeed)| isWall(maze, self.rect.x + (3/4)*self.width, self.rect.y + self.height + gamespeed) | isWall(maze, self.rect.x + self.width, self.rect.y + self.height + gamespeed)):
            return False
        if (direction == "left") & (isWall(maze, self.rect.x - gamespeed, self.rect.y) |isWall(maze, self.rect.x - gamespeed, self.rect.y + self.height/4) | isWall(maze, self.rect.x - gamespeed, self.rect.y + self.height/2) |isWall(maze, self.rect.x - gamespeed, self.rect.y + (3/4)*self.height)| isWall(maze, self.rect.x - gamespeed, self.rect.y + self.height)):
            return False
        if (direction == "right") & (isWall(maze, self.rect.x + self.width + gamespeed, self.rect.y) | isWall(maze, self.rect.x +self.width + gamespeed, self.rect.y + self.height/4) | isWall(maze, self.rect.x +self.width + gamespeed, self.rect.y + self.height/2) | isWall(maze, self.rect.x +self.width + gamespeed, self.rect.y + (3/4)*self.height) | isWall(maze, self.rect.x + self.width + gamespeed, self.rect.y + self.height)):
            return False

        return True

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


class Hazard(Player):
    #this should have Player as its parent class, as of now I don't know how to do that- will work on it
    def getCollision(self, dragon):

        collision_Sound = pygame.mixer.Sound('Dragon_roar.wav')

        if pygame.sprite.collide_rect(self, dragon):
            print("hit")
            dragon.lives - 1
            collision_Sound.play()
            if dragon.rect.x > self.width/2:
                x_Dragon  = self.rect.right + gamespeed
            if dragon.rect.x < self.width/2:
                x_Dragon = self.rect.left - self.width - gamespeed
            if dragon.rect.y + dragon.height > self.height/2:
                y_Dragon = self.rect.top - dragon.height - gamespeed
            if dragon.rect.y > self.height/2:
                y_Dragon = self.rect.bottom + gamespeed






#Checks to see if the coordinates are in a wall
#Parameters are x and y coordinates of the points to be tested
def isWall(maze, x, y):

    #going to check if x y is in any of the walls
    #returns true if the point is inside the wall

    for wall in maze:

        if (x > wall.x) & (x < wall.x + wall.width) & (y > wall.y) & (y < wall.y + wall.height):
            return True


    return False


# Defines class for static images in bottom player info display
class BottomDisplayImage(pygame.sprite.Sprite):

    def __init__(self, filename, size, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert() # Load image
        self.image.set_colorkey([0, 0, 0]) # Set transparency
        self.image = pygame.transform.scale(self.image, size) # Resize sprite
        self.rect = self.image.get_rect(center=(location[0] + (size[0] / 2), location[1] + (size[1] / 2))) # Create rectangle around sprite
        # Image location
        self.rect.x = location[0]
        self.rect.y = location[1]



class EndMarker(pygame.sprite.Sprite):      
    
    def __init__(self, color, filename, location):
        # call parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(filename).convert_alpha()
        # make 'color' transparent on the image
        self.image.set_colorkey(color) 
        # resize image to 20x20 px
        self.image = pygame.transform.scale(self.image, (20,20))
        
        # set the rectangle defined for this image for collision detection
        self.rect = self.image.get_rect()
        # position the image
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    def getCollision(self, theDragon, dragon_choice, sound_choice, start_coords, end_coords):
        if pygame.sprite.collide_rect(self, theDragon):

            global state, room, livesLeft
            livesLeft = 3
            if room == 2:
                state = 1
                room = 0
                EndScreen.YouWin(dragon_choice, sound_choice)
            else:
                room += 1
                PlayGame(start_coords[room][0], start_coords[room][1], dragon_choice, sound_choice)
        
        
class Wall(pygame.sprite.Sprite):

    def __init__(self, x_wall, y_wall, x_width, y_length):


        pygame.sprite.Sprite.__init__(self)
        self.width = x_width
        self.height = y_length
        self.x = x_wall
        self.y = y_wall
        self.image = pygame.Surface([x_width, y_length])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()        
        self.rect.x = x_wall
        self.rect.y = y_wall

mazes = []
# implementation inspired by simpson college CS





# returns True when the player is DONE colliding with a wall
# (prevents the wallCollisionCount from constantly increasing if the player holds down a key running into the wall)
def countCollision(key, count, dragon, endCake): # TODO: fix this
    global x_Dragon
    global y_Dragon
    global gamespeed

    while (True): # wait for KEYUP
        screen.fill([255,255,255])
        mazes[room].draw(screen)
        screen.blit(endCake.image, endCake)
        # Bottom display
        for i in range (0, livesLeft): # Displays as many hearts as lives left
            heart = BottomDisplayImage("Resources/heart.png",(30, 30), (115 + (i * 35), 475))
            screen.blit(heart.image, heart)
        livesLeftText = BottomDisplayImage ("Resources/livesLeftText.png", (110, 28), (10, 475))
        screen.blit(livesLeftText.image, livesLeftText)
        dragon.rect.x = x_Dragon
        dragon.rect.y = y_Dragon
        timer = pygame.time.get_ticks()
        dragon.updateAnimation(timer)
        pygame.display.update()

        pressed = pygame.key.get_pressed()

        if pressed[dragon.upkey]:
            if dragon.canMove("up", mazes[room]):
                y_Dragon -= gamespeed

        if pressed[dragon.downkey]:
            if dragon.canMove("down", mazes[room]):
                y_Dragon += gamespeed

        if pressed[dragon.leftkey]:
            if dragon.canMove("left", mazes[room]):
                x_Dragon -= gamespeed

        if pressed[dragon.rightkey]:
            if dragon.canMove("right", mazes[room]):
               x_Dragon += gamespeed

        for event in pygame.event.get():
            if event.type == KEYUP and event.key == key:
                return count + 1



global room
room = 0

def PlayGame(x_Start, y_Start, dragon_choice, sound_choice):
    #Will play the music
    if(sound_choice == 1):
        print "sound choice is 1 should be jamming"
        bg_music = pygame.mixer.music
        bg_music.load('background_music.wav')
        print "should play music"
        #-1 will loop indefinitely, otherwise number will be numb loops after first play through
        # 0.0 the time where the wav begins playing
        bg_music.play(-1, 0.0)
    
    collision_Sound = pygame.mixer.Sound('Dragon_roar.wav')
    
    global x_Dragon
    global y_Dragon
    #global coll
    x_Dragon = x_Start
    y_Dragon = y_Start

    wall_list_1 = pygame.sprite.Group()
    wall_1 = [#[30, 30, 5, 410], #left
       # [30, 440, 640, 5], #bottom
      #  [30, 30, 640, 5], #top
       # [670, 30, 5, 415 ],        #right
        [0, 330, 605, 10],
        [266, 387, 300, 10],
        [595, 85, 10, 255],
        [95, 82, 510,10],
        [94, 82, 10, 190],
        [94, 272, 440, 10],
        [528, 140, 10, 142],
        [-10, 450, 710, 10],
        [160, 140, 375, 10],
        [160, 140, 10, 65],
        [160, 200, 300, 10]
        
        # start 30,396
        # end 180, 171
        ]
            # add each part of wall to a list
    for var in wall_1:
        wall = Wall(var[0], var[1], var[2], var[3])
        wall_list_1.add(wall)
    mazes.append(wall_list_1)

    start_coords = []
    start_coords.append((30,396))
    end_coords = []
    end_coords.append((180,171))


    wall_list_2 = pygame.sprite.Group()
    wall_2 = [#[30, 30, 5, 410], #left
       # [30, 440, 640, 5], #bottom
       # [30, 30, 640, 5], #top
       # [670, 30, 5, 415 ], #right
        [-10, 450, 710, 10],
        [-10, 385, 532, 10],
        [585, 385, 60, 10],
        [30, 385, 490, 10],
        [515, 215, 10, 180],
        [515, 300, 80, 10],
        [250, 215, 270, 10],
        [385, 120, 10, 102],
        [590, 120, 10, 100],
        [515, 120, 80, 10],
        [515, -10, 10, 135],
        [150, 120, 100, 10],
        [150, 120, 10, 180],
        #[150, 300, 300, 5],
        [-10, 120, 100, 10],
        [90, 120, 10, 184],
        [90, 296, 333, 10],
        #end maze at 64,150

        ]
            # add each part of wall to a list
    for var in wall_2:
        wall = Wall(var[0], var[1], var[2], var[3])
        wall_list_2.add(wall)
    mazes.append(wall_list_2)
    start_coords.append((61,414))
    end_coords.append((64,150))
    wall_list_3 = pygame.sprite.Group()
    wall_3 = [#[30, 30, 5, 410], #left
        #[30, 440, 640, 5], #bottom
        #[30, 30, 640, 5], #top
       # [670, 30, 5, 415 ], #right
        [-10, 450, 710, 10],
        [95, 393, 10, 60],
        [-10, 330, 170, 10],
        [160, 330, 10, 54],
        [233, 90, 10, 365],
        [95, 90, 145, 10],
        [95, 90, 10, 150],
        [95, 240, 73, 10],
        [350, 90, 10, 280],
        [350, 90, 225, 10],
        [350, 370, 230, 10],
        [575, 90, 10, 68],
        [575, 305, 10, 75],
        [293, 90, 10, 284],
        [420, 145, 10, 165],
        [420, 240, 300, 10],
        [420, 305, 160, 10],
        [420, 190, 90, 10],
        #end at 551,343
        ]
            # add each part of wall to a list
    for var in wall_3:
        wall = Wall(var[0], var[1], var[2], var[3])
        wall_list_3.add(wall)
    mazes.append(wall_list_3)
    start_coords.append((41,404))
    end_coords.append((537,341))
    #just a testing screen
    wall_list_test = pygame.sprite.Group()
    wall_test = [[400, 90, 90, 10], [60, 400, 5, 400]]
    for var in wall_test:
        wall = Wall(var[0], var[1], var[2], var[3])
        wall_list_test.add(wall)
    mazes.append(wall_list_test)

    #Looks at the players choice of dragon and goes and gets that picture
    #And changes width/height accordingly
    if(dragon_choice=="orange"):
        dragon = Player((255,255,255), 36, 32, "Resources/OrangeDragon.png", [x_Dragon, y_Dragon], 0)
    elif(dragon_choice=="black"):
        dragon = Player((255,255,255), 36, 32, "Resources/BlackDragon.png", [x_Dragon, y_Dragon], 0)
    elif(dragon_choice=="red"):
        dragon = Player((255,255,255), 36, 32, "Resources/RedDragon.png", [x_Dragon, y_Dragon], 0)
    elif(dragon_choice=="greenandblue"):
        dragon = Player((255,255,255), 36, 32, "Resources/GreenAndBlueDragon.png", [x_Dragon, y_Dragon], 0)

    endCake = EndMarker((225,255,255), "Resources/Cake.png",  end_coords[room])
    screen.blit(dragon.image, dragon)
    screen.blit(endCake.image, endCake)


    # knight = Hazard([255,255,255], 20, 20, "Resources/explosiongif.png", [750,750], 0) # TODO: uncomment


    global state
    global livesLeft
    global badkeycount
    badkeycount = 0
    global wallCollisionCount
    wallCollisionCount = 0
    global keyHints
    keyHints = False
    state = 0



    while state != 1:

        #Just a white screen
        screen.fill([255,255,255])
         #create the dragon image
        if keyHints:
            showKeys(dragon, screen)
        screen.blit(endCake.image, endCake)
        endCake.getCollision(dragon, dragon_choice, sound_choice, start_coords, end_coords)



        dragon.rect.x = x_Dragon
        dragon.rect.y = y_Dragon



        # screen.blit(knight.image, knight)
        # knight.rect.x = 400
        # knight.rect.y = 400
        # knight.getCollision(dragon)
        # TODO: uncomment this





        timer = pygame.time.get_ticks()

        dragon.updateAnimation(timer)

        mazes[room].draw(screen)


        # Bottom display
        for i in range (0, livesLeft): # Displays as many hearts as lives left
            heart = BottomDisplayImage("Resources/heart.png",(30, 30), (115 + (i * 35), 475))
            screen.blit(heart.image, heart)
        livesLeftText = BottomDisplayImage ("Resources/livesLeftText.png", (110, 28), (10, 475))
        screen.blit(livesLeftText.image, livesLeftText)


        pygame.display.update()

        keypressed = pygame.key.get_pressed()


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


            if event.type == KEYDOWN and keyHints == False:
                checkKey = event.key
                if checkKey != dragon.upkey and checkKey != dragon.downkey and checkKey != dragon.leftkey and checkKey != dragon.rightkey:
                    badkeycount += 1
                    print badkeycount
                    if badkeycount >= 10:
                        keyHints = True


        if keypressed[dragon.upkey]:
            if dragon.canMove("up", mazes[room]):
                y_Dragon -= gamespeed
            if((dragon.canMove("up", mazes[room])) == False):
                if(sound_choice==1):
                    collision_Sound.play()
                wallCollisionCount = countCollision(dragon.upkey, wallCollisionCount, dragon, endCake)


        if keypressed[dragon.downkey]:
            if dragon.canMove("down", mazes[room]):
                y_Dragon += gamespeed
            if((dragon.canMove("down", mazes[room]))==False):
                if(sound_choice==1):
                    collision_Sound.play()
                wallCollisionCount = countCollision(dragon.downkey, wallCollisionCount, dragon, endCake)

        if keypressed[dragon.leftkey]:
            if dragon.canMove("left", mazes[room]):
                x_Dragon -= gamespeed
            if((dragon.canMove("left", mazes[room]))==False):
                if(sound_choice==1):
                    collision_Sound.play()
                wallCollisionCount = countCollision(dragon.leftkey, wallCollisionCount, dragon, endCake)



        if keypressed[dragon.rightkey]:
           if dragon.canMove("right", mazes[room]):
               x_Dragon += gamespeed
           if((dragon.canMove("right", mazes[room]))==False):
                if(sound_choice==1):
                    collision_Sound.play()
                wallCollisionCount = countCollision(dragon.rightkey, wallCollisionCount, dragon, endCake)

        if keyHints == False and wallCollisionCount >= 5:
            keyHints = True
