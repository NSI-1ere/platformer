import pygame as pg

class Constantes:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.SCREEN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Platformer")
        self.CLOCK = pg.time.Clock()
        self.FPS = 60