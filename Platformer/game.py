import pygame as pg
import sys
import subprocess
from player import Player
from constantes import Constantes
from platforms import PlatformsManager

class Game:
    def __init__(self):
        self.player = Player()
        self.const = Constantes()
        self.platform_manager = PlatformsManager()
        self.clock = self.const.CLOCK
        self.running = True
        #self.gameover_file = sys.path.append('/platformer/gameover.py')

    def run(self):
        while self.running:
            # Gestion des événements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    #subprocess.run(self.gameover_file)

            # Mise à jour
            self.player.update(self.platform_manager.platforms)

            # Dessin
            self.const.SCREEN.fill(self.const.WHITE)
            self.platform_manager.draw_platforms()
            self.player.draw()

            # Défilement vertical
            if self.player.y < self.const.HEIGHT // 3:
                offset = self.const.HEIGHT // 3 - self.player.y
                self.player.y += offset
                for platform in self.platform_manager.platforms:
                    platform.y += offset

            # Rafraîchissement
            pg.display.flip()
            self.const.CLOCK.tick(self.const.FPS)

        pg.quit()
        sys.exit()