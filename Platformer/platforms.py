import pygame as pg
from constantes import Constantes

class PlatformsManager:
    def __init__(self):
        self.const = Constantes()
        self.platforms = [
            pg.Rect(200, 500, 400, 20),
            pg.Rect(50, 400, 150, 20),
            pg.Rect(600, 350, 200, 20),
            pg.Rect(0, 300, 100, 20),
            pg.Rect(200, 200, 200, 20),
        ]

    def draw_platforms(self):
        for platform in self.platforms:
            pg.draw.rect(self.const.SCREEN, self.const.BLUE, platform)
        #print(platforms)
