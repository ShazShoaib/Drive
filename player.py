import pygame
import math
import helper
from settings import *

class player:
    def __init__(self):
        self.alive = True
        self.x = SCREEN_WIDTH * 5 / 123 + (SCREEN_WIDTH * 28 / 123 - CAR1_WIDTH) / 2 + 2 * SCREEN_WIDTH * 28 / 123
        self.y = SCREEN_HEIGHT-CAR2_HEIGHT
        self.img_path = PLAYER_IMG_PATH
        self.img = pygame.image.load(self.img_path)
        self.angle = 0
        self.Vx = 0
        self.Vy = 0
        self.w = CAR2_WIDTH
        self.h = CAR2_HEIGHT


    def update(self):
        self.x = self.x + self.Vx
        self.y = self.y + self.Vy

        self.Vx = self.Vx * 0.8
        self.Vy = self.Vy * 0.9


        helper.bound_screen_space(self)
        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation

        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (self.w * scaler, self.h * scaler))                 # Scale the image according to its width and height


    def render(self,window):
        window.blit(self.img, (self.x, self.y))
