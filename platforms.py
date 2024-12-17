import pygame as pg
from constantes import Constantes
from random import randint

class PlatformsManager:
    def __init__(self):
        self.const = Constantes()
        self.starter_platform = pg.Rect(pg.display.Info().current_w/2 - 200, pg.display.Info().current_h-100, 400, 20)
        self.platforms = [
            self.starter_platform,
        ]

    def gen_platform(self, previous_platform):
        #Can jump and move ~100
        left_or_right = randint(0, 1)
        if left_or_right == 0:
            left = randint(previous_platform.left - 120, previous_platform.left - 80)
        else: 
            left = randint(previous_platform.left + 80, previous_platform.left + 120)
        top = randint(previous_platform.top - 90, previous_platform.top - 80)
        width = randint(100, 200)
        if left - width < 0:
            left = randint(previous_platform.left, previous_platform.left + 120)
        elif left + width > pg.display.Info().current_w:
            left = randint(previous_platform.left - 120, previous_platform.left)
        new_platform = pg.Rect(left, top, width, 20)
        self.platforms.append(new_platform)

    def draw_platforms(self):
        for platform in self.platforms:
            pg.draw.rect(self.const.SCREEN, self.const.BLUE, platform, border_radius=3)
