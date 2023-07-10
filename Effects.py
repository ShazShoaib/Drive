from settings import *
import helper
import math
import pygame


class effect:
    def __init__(self, player):
        self.alive = True
        self.status_on = False
        self.img_path = NOS_IMG_PATHS
        self.cooldown = 7
        self.curr_frames = 0
        self.index = 0
        self.angle = 0
        self.img = pygame.image.load(self.img_path[self.index])
        self.car = player

    def tick(self,frames):
        self.curr_frames = self.curr_frames + frames
        if self.curr_frames > self.cooldown:
            self.index = self.index + 1
            self.curr_frames = 0
            if self.index >= len(self.img_path):
                self.index = 0

    def update(self):
        scaler = 1 + (math.sqrt(2) - 1) * abs(
            math.sin(2 * helper.to_radian(self.angle)))  # A scaler to keep the scale constant after rotation

        self.img = pygame.image.load(self.img_path[self.index])  # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)  # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (
        self.car.w * scaler, self.car.h * scaler))  # Scale the image according to its width and height


    def render(self,window):
        if self.status_on:
            window.blit(self.img, (self.car.x, self.car.y))