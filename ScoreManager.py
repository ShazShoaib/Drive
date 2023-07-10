import pygame.image

import helper
from TextObj import *
from speedManager import *
import math
from speedManager import *
class score():

    def __init__(self,text):
        self.alive = True
        self.txtobj = txt_obj(text)
        self.SM = speedMan()

        self.img_path = SCORE_IMG_PATH
        self. w = 150
        self.h = 50
        self.x = SCREEN_WIDTH - 150
        self.y = 0
        self.angle = 0
        self.txtobj.x = self.x + self.w
        self.curr_score = 0

        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation
        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (
        self.w * scaler, self.h * scaler))                                                              # Scale the image according to its width and height

    def update(self):
        self.curr_score = self.curr_score + self.SM.getSpeed()
        speedtxt = helper.SetNoDigits(int(self.curr_score/100),6)
        self.txtobj.text = str(speedtxt)
        self.txtobj.x = self.x + self.w/2 -self.txtobj.rect.w -32
        self.txtobj.y = self.y + self.h/4 -2
        self.txtobj.update()


        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation
        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (self.w * scaler, self.h * scaler))                 # Scale the image according to its width and height


    def render(self,window):
        window.blit(self.img, (self.x, self.y))
        self.txtobj.render(window)