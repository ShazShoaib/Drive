import pygame

from speedManager import *
from settings import *


class Nos:
    def __init__(self):
        self.alive = True
        self.isNos = True
        self.color = (255, 0, 0, 255)

    def update(self):
        if self.isNos:
            SM = speedMan()
            SM.add(2/FPS)

    def render(self, window):
        if self.isNos:
            rect_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            rect_surface.set_alpha(32)
            rect_surface.fill((0,0,128))
            window.blit(rect_surface,(0,0))
