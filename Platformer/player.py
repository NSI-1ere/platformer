import pygame as pg
import sys
from platforms import PlatformsManager
from constantes import Constantes

# Classe Joueur
class Player:
    def __init__(self):
        self.platform_manager = PlatformsManager()
        self.const = Constantes()
        self.width = 50
        self.height = 50
        # Placer le joueur sur la première plateforme
        starting_platform = self.platform_manager.platforms[0]  # Choisir la première plateforme
        self.x = starting_platform.left + (starting_platform.width - self.width) // 2  # Centré horizontalement
        self.y = starting_platform.top - self.height  # Juste au-dessus de la plateforme 
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 0.5 
        self.on_ground = True

    def handle_input(self):
        keys = pg.key.get_pressed()

        # Déplacements horizontaux
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed

        # Saut
        if keys[pg.K_SPACE] and self.on_ground:
            self.velocity_y = -10
            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

    def check_collision(self):
        self.on_ground = False
        for platform in self.platform_manager.platforms:
            if (
                self.y + self.height >= platform.top
                and self.y + self.height <= platform.bottom
                and self.x + self.width > platform.left
                and self.x < platform.right
            ):
                self.y = platform.top - self.height
                self.velocity_y = 0
                self.on_ground = True

    def update(self):
        self.handle_input()
        self.apply_gravity()
        self.check_collision()

    def draw(self):
        pg.draw.rect(self.const.SCREEN, self.const.BLACK, (self.x, self.y, self.width, self.height))