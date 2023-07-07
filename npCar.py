import random
import pygame
import math
import helper
from settings import *

class car:
    car_paths = [CAR_IMG_PATH_G,CAR_IMG_PATH_B, CAR_IMG_PATH_R, CAR_IMG_PATH_Y, CAR_IMG_PATH_W]
    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 0
        self.img_path = self.car_paths[random.randint(0,len(self.car_paths)-1)]
        self.img = pygame.image.load(self.img_path)
        self.angle = 0
        self.Vx = 0
        self.Vy = NP_CAR_SPEED * random.randint(5,10)/5
        self.w = CAR1_WIDTH
        self.h = CAR1_HEIGHT
        self.row = -1

    def update(self):
        self.y = self.y + self.Vy

        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation

        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (self.w * scaler, self.h * scaler))                 # Scale the image according to its width and height


    def render(self,window):
        window.blit(self.img, (self.x, self.y))


