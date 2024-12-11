import pygame as pg
import tkinter as tk

class Constantes:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.COIN_WIDTH = 20
        self.COIN_HEIGHT = 20
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.SCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption("Platformer")
        self.CLOCK = pg.time.Clock()
        self.FPS = 60