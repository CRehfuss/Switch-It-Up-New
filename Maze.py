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