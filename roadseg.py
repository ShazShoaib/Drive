import pygame
from settings import *
from speedManager import *

class roadSeg:
    def __init__(self):
        global ROAD_SPEED
        self.alive = True
        self.img_path = 'sprites/rd.png'
        self.img = pygame.image.load(self.img_path)
        self.y = 0
        self.x = 0
        SM = speedMan()
        self.Vy = SM.getSpeed()
        self.w = SCREEN_WIDTH
        self.h = SCREEN_HEIGHT
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

    def update(self):
        self.y = self.y + self.Vy

    def render(self,window):
        window.blit(self.img, (self.x, self.y))

class road:
    def __init__(self):
        self.alive = True
        self.seg_list = []
        R1 = roadSeg()
        R2 = roadSeg()
        R2.y = -SCREEN_HEIGHT
        self.seg_list.append(R1)
        self.seg_list.append(R2)

    def update(self):
        for seg in self.seg_list:
            seg.update()

        if (self.seg_list[-1].y > 0):
            Rd = roadSeg()
            Rd.y = -SCREEN_HEIGHT+ROAD_SPEED
            self.seg_list.append(Rd)
            del self.seg_list[0]

    def render(self,window):
        for seg in self.seg_list:
            seg.render(window)