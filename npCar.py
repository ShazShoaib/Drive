import pygame
import math
import helper

class car:
    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 0
        self.img_path = 'sprites/car1.png'
        self.img = pygame.image.load(self.img_path)
        self.angle = 0
        self.Vx = 0
        self.Vy = 2
        self.w = 96
        self.h = 120

    def update(self):
        self.y = self.y + self.Vy

        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation

        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (self.w * scaler, self.h * scaler))                 # Scale the image according to its width and height


    def render(self,window):
        window.blit(self.img, (self.x, self.y))