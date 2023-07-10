import pygame

import NosManager
from settings import *
from roadseg import *
from player import *
from helper import *
from VehicleManager import *
from Speedometer import *
from NosManager import *
from Effects import *
from ScoreManager import *

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

obj_list = []  # Stores all game objects
P = player()
VM = carManager()
Rd = road()
SM = speedMan()
SP = speedometer(str(SM.getSpeed()))
NS = Nos()
EFF = effect(P)
SCO = score("0")

obj_list.append(Rd)
obj_list.append(P)
obj_list.append(VM)
obj_list.append(SP)
obj_list.append(NS)
obj_list.append(EFF)
obj_list.append(SCO)
running = True  # manages when the game runs/ends
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        set_input(event)
    manage_input(P, obj_list,VM,NS,EFF)  # Player Input is managed in a helper function

    SM.add(1/FPS)          # gradually increase game speed
    EFF.tick(1)


    for i in range(len(obj_list) - 1, 0, -1):  # remove all items which are marked as destroyed
        if not obj_list[i].alive:
            del obj_list[i]

    VM.collision_check(P)
    for game_obj in obj_list:  # Update all game objects
        game_obj.update()

    window.fill((0, 0, 0))  # Clear the window

    for image in obj_list:
        image.render(window)  # Render the image onto the window

    pygame.display.flip()  # Update the display

    clock.tick(FPS)

pygame.quit()
