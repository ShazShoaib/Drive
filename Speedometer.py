import pygame.image

import helper
from TextObj import *
from speedManager import *
import math
class speedometer():

    def __init__(self,text):
        self.alive = True
        self.txtobj = txt_obj(text)
        self.SM = speedMan()

        self.img_path = SPEEDOMETER_IMG_PATH
        self. w = 100
        self.h = 50
        self.x = SCREEN_WIDTH/2 - self.w/2
        self.y = 0
        self.angle = 0

        self.txtobj.x = self.x + self.w

        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation
        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (
        self.w * scaler, self.h * scaler))                                                              # Scale the image according to its width and height

    def update(self):
        speedtxt = helper.SetNoDigits(int(self.SM.getSpeed()*SPEEDOMETER_ACCELERATION),3)
        speedcolor = helper.limitTo(self.SM.getSpeed()*SPEEDOMETER_COLOR_CHANGE, 255)
        self.txtobj.text = str(speedtxt)
        self.txtobj.color[0] = (speedcolor, 255 - speedcolor, 255 - speedcolor)
        self.txtobj.x = self.x + self.w/2 -self.txtobj.rect.w -3
        self.txtobj.y = self.y + self.h/4 -2
        self.txtobj.update()


        scaler = 1 + (math.sqrt(2) - 1) * abs(math.sin(2 * helper.to_radian(self.angle)))               # A scaler to keep the scale constant after rotation
        self.img = pygame.image.load(self.img_path)                                                     # Load the image again to minimize artifacting
        self.img = pygame.transform.rotate(self.img, self.angle)                                        # Rotate the image according to its angle
        self.img = pygame.transform.scale(self.img, (self.w * scaler, self.h * scaler))                 # Scale the image according to its width and height


    def render(self,window):
        window.blit(self.img, (self.x, self.y))
        self.txtobj.render(window)

