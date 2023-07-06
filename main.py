import pygame
from settings import *
from roadseg import *
from player import *
from helper import *
from VehicleManager import *

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

obj_list = []  # Stores all game objects
P = player()
E = carManager()
Rd = road()
SM = speedMan()

obj_list.append(Rd)
obj_list.append(P)
obj_list.append(E)

running = True  # manages when the game runs/ends
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        set_input(event)
    manage_input(P, obj_list)  # Player Input is managed in a helper function

    SM.add(1/FPS)          # gradually increase game speed

    for i in range(len(obj_list) - 1, 0, -1):  # remove all items which are marked as destroyed
        if not obj_list[i].alive:
            del obj_list[i]

    for game_obj in obj_list:  # Update all game objects
        game_obj.update()

    window.fill((0, 0, 0))  # Clear the window

    for image in obj_list:
        image.render(window)  # Render the image onto the window

    pygame.display.flip()  # Update the display

    clock.tick(FPS)

pygame.quit()
