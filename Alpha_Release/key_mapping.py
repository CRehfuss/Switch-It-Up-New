# Main calls this class to get the key mapping, up down left right, for the game that is being played
# This could be called in the initialization of a player, and have the keys as attributes of the object
# i.e. player.up, player.down, player.right, player.left = getUp()
# would give the player the keys necessary for moving around.
#

import pygame, random
from pygame.locals import *



arrowkeys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
allalphabetkeys = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p,K_q, K_r, K_s, K_t, K_u,
                K_v, K_w, K_x, K_y, K_z]
numberkeys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]


def getKeys(difficulty):


    if difficulty == 0:
        up = K_UP
        down = K_DOWN
        left = K_LEFT
        right = K_RIGHT

    if difficulty == 1:
        random.shuffle(arrowkeys)
        up = arrowkeys[0]
        down = arrowkeys[1]
        left = arrowkeys[2]
        right = arrowkeys[3]

    if difficulty == 2:
        up = K_w
        down = K_s
        left = K_a
        right = K_d

    if difficulty == 10:
        random.shuffle(allalphabetkeys)
        up = allalphabetkeys[0]
        down = allalphabetkeys[1]
        left = allalphabetkeys[2]
        right = allalphabetkeys[3]

    return up, down, left, right #this is mapped out North south east west