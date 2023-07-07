import pygame
from settings import *

class txt_obj:

    pygame.init()
    font = pygame.  font.Font('freesansbold.ttf', 32)

    def __init__(self,text):
        self.alive = True
        self.text = text
        self.color = [(255, 255, 255), (0, 0, 0)]
        self.text_surface = self.font.render(self.text, True, self.color[0])
        self.rect = self.text_surface.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.x = 0
        self.y = 0
        self.width = 25
        self.height = 30

    def clicked(self,x,y):
        if (x > self.x and x < self.x + self.width):
            if( y > self.y and y < self.y + self.height):
                return True
        return False

    def update(self):
        self.text_surface = self.font.render(self.text, True, self.color[0])
        self.rect = self.text_surface.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.width
        self.rect.height = self.height

    def render(self,window):
        window.blit(self.text_surface, self.rect)