import pygame
import math
from settings import *
from speedManager import *

def to_radian(angle):                                       # converts degree to radian units
    return math.pi*angle/180

keys = {                                    # The list of keys for input
    "up": False,                            # UP arrow key
    "down": False,                          # DOWN arrow key
    "left": False,                          # LEFT arrow key
    "right": False,                         # RIGHT arrow key
    "enter": False,                         # ENTER key
    "space": False,                         # SPACEBAR key
    "f": False                              # F key
}

def set_input(event):                                       # Set the keys as pressed or no pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            keys['up'] = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            keys['down'] = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            keys['left'] = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            keys['right'] = True
        elif event.key == pygame.K_SPACE:
            keys['space'] = True
        elif event.key == pygame.K_f:
            keys['f'] = True


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            keys['up'] = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            keys['down'] = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            keys['left'] = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            keys['right'] = False
        elif event.key == pygame.K_SPACE:
            keys['space'] = False
        elif event.key == pygame.K_f:
            keys['f'] = False

def manage_input(player,obj_list):
    global ROAD_SPEED
    if(not player.alive):
        return
    # MOVEMENT CONTROLS
    if keys['up']:
        player.Vy = player.Vy - 1
    if keys['down']:
        player.Vy = player.Vy + 1
    if keys['left']:
        player.Vx = player.Vx - 1
    if keys['right']:
        player.Vx = player.Vx + 1

    # COMPOUND MOVEMENT CONTROLS, MULTIPLE KEYS PRESSED
    if keys['up']:
        if keys['left']:
            pass
        if keys['right']:
            pass
    if keys['down']:
        if keys['left']:
            pass
        if keys['right']:
            pass

    # SPECIAL ACTIONS
    if keys['space']:
        SM = speedMan()
        SM.mul(60*BRAKE_FORCE/FPS)
    if keys['f']:
        pass #player.attack(obj_list)

def bound_check(game_object,X_UB=SCREEN_WIDTH,Y_UB=SCREEN_HEIGHT,X_LB=0,Y_LB=0):
    if (game_object.x + game_object.w >= X_UB):
        return False
    elif (game_object.x <= X_LB):
        return False
    if (game_object.y + game_object.h >= Y_UB):
        return False
    elif (game_object.y <= Y_LB):
        return False
    return True

def bound_screen_space(game_object):
    if (game_object.x + game_object.w >= SCREEN_WIDTH):
        game_object.x = SCREEN_WIDTH - game_object.w
        game_object.Vx = -game_object.Vx
    elif (game_object.x <= 0):
        game_object.x = 0
        game_object.Vx = -game_object.Vx

    if (game_object.y + game_object.h >= SCREEN_HEIGHT):
        game_object.y = SCREEN_HEIGHT - game_object.h
        game_object.Vy = -game_object.Vy
    elif (game_object.y <= 0):
        game_object.y = 0
        game_object.Vy = -game_object.Vy



def collide_check(object1,object2):                         # checks whether two objects are colliding with each other

    if (abs(object1.x + object1.w * 0.5 - object2.x - object2.w * 0.5)) < 0.5*(object1.w + object2.w) and \
       (abs(object1.y + object1.h * 0.5 - object2.y - object2.h * 0.5)) < 0.5 * (object1.h + object2.h):
            return True
    return False

def collide_check_exp(player,car):                         # checks whether two objects are colliding with each other

    front_collide = False
    back_collide = False
    right_collide = False
    left_collide = False
    if abs(player.y - (car.y + car.h)) > 5:
        front_collide = True
    if abs((player.y + player.h) - car.y) > 5:
        back_collide = True
    if abs(player.x - (car.x + car.w)) > 5:
        left_collide = True
    if abs(player.x + (player.w - car.x)) > 5:
        right_collide = True

    return front_collide,back_collide,left_collide,right_collide

