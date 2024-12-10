import sys, os, subprocess, pygame as pg
from player import Player
from constantes import Constantes
from platforms import PlatformsManager
from load_background import load_background

class Game:
    def __init__(self):
        self.player = Player()
        self.const = Constantes()
        self.platform_manager = PlatformsManager()
        self.bkgrnd = load_background()
        self.clock = self.const.CLOCK
        self.running = True
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.impact_font = self.chemin_repertoire + r".\impact.ttf"
        self.pause_inputs = False

        # Charger les frames du GIF
        self.frames = self.bkgrnd.load_gif(self.chemin_repertoire + r'.\Clouds.gif')
        self.frame_index = 0
        #self.gameover_file = sys.path.append('/platformer/gameover.py')

    def run(self):
        while self.running:

            # Gestion des événements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.running = False
                    #subprocess.run(self.gameover_file)

            # Mise à jour
            self.player.update(self.platform_manager.platforms)

            # Dessin
            self.const.SCREEN.fill((0, 0, 0))
            self.const.SCREEN.blit(self.frames[self.frame_index], (0, 0))
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.platform_manager.draw_platforms()
            self.player.draw()

            # Défilement vertical
            if self.player.y < self.const.HEIGHT // 3:
                offset = self.const.HEIGHT // 3 - self.player.y
                self.player.y += offset
                for platform in self.platform_manager.platforms:
                    platform.y += offset

            if self.player.check_if_gameover():
                font = pg.font.Font(self.impact_font, 100)
                text = font.render("Game Over!", True, self.const.RED)
                text_rect = text.get_rect(center=(pg.display.Info().current_w // 2, pg.display.Info().current_h // 2))
                self.const.SCREEN.blit(text, text_rect)

                font2 = pg.font.Font(self.impact_font, 50)
                text2 = font2.render("Please press Enter to retry.", True, self.const.WHITE)
                text2_rect = text2.get_rect(center=(pg.display.Info().current_w // 2, pg.display.Info().current_h // 2 + text_rect.height - 20))
                self.const.SCREEN.blit(text2, text2_rect)

            # Rafraîchissement
            pg.display.flip()
            self.const.CLOCK.tick(self.const.FPS)
        else:
            pg.quit()
            sys.exit()