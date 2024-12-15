import sys, os, subprocess, pygame as pg
from player import Player
from constantes import Constantes
from platforms import PlatformsManager
from coins import CoinsManager
from load_background import load_background
from sprite import Sprite


class Game:
    def __init__(self):
        self.player = Player()
        self.const = Constantes()
        self.platform_manager = PlatformsManager()
        self.coins_manager = CoinsManager()
        self.bkgrnd = load_background()
        self.sprites = Sprite()
        self.scrolling_to_reverse = []
        self.clock = self.const.CLOCK
        self.running = True
        self.chemin_repertoire = os.path.dirname(os.path.abspath(__file__))
        self.impact_font = self.chemin_repertoire + r".\impact.ttf"
        self.pause_inputs = False
        self.is_paused = False
        self.gameover = False
        self.gamewon = False
        self.pause_iteration = 0
        self.background =  pg.image.load(self.chemin_repertoire + r".\Background.jpg")

        # Charger les frames du GIF
        #self.frames = self.bkgrnd.load_gif(self.chemin_repertoire + r".\Clouds.gif")
        #self.frame_index = 0

        # Obtenir les dimensions actuelles de l'écran
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()
        # Redimensionner l'image de l'arrière-plan aux dimensions de l'écran 
        self.resized_background = pg.transform.scale(self.background, (self.screen_width, self.screen_height))

    # On vide le terminal (Esthetique uniquement)
    os.system("cls" if os.name == "nt" else "clear")
    
    def run(self):
        self.sprites.set_center(self.player.x, self.player.y)
        while self.running:

            #Textes

            font = pg.font.Font(self.impact_font, 100)
            text = font.render("Game Over!", True, self.const.RED)
            text_rect = text.get_rect(
                center=(
                    pg.display.Info().current_w // 2,
                    pg.display.Info().current_h // 2,
                )
            )
            font2 = pg.font.Font(self.impact_font, 50)
            text2 = font2.render(
                "Please press Enter to retry.", True, self.const.WHITE
            )
            text2_rect = text2.get_rect(
                center=(
                    pg.display.Info().current_w // 2,
                    pg.display.Info().current_h // 2 + text_rect.height - 20,
                )
            )
            text_win = font.render("Game Won!", True, self.const.GREEN)
            text_win_rect = text_win.get_rect(
                center=(
                    pg.display.Info().current_w // 2,
                    pg.display.Info().current_h // 2,
                )
            )
            font_coin = pg.font.Font(self.impact_font, 50)
            text_coin = font_coin.render(f"{self.player.coins_counter}", True, self.const.BLACK)
            text_coin_rect = text_coin.get_rect()
            text_coin_rect.topright = (self.const.SCREEN.get_width() - 10, 10)

            platforms = self.platform_manager.platforms

            # Gestion des événements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                    if self.is_paused and event.key == pg.K_RETURN:
                        subprocess.run(["python", self.chemin_repertoire + r".\main.py"])
                        self.running = False

            # Récupérer les touches pressées
            touches = pg.key.get_pressed()

            # Mise à jour
            self.player.update(
                self.platform_manager.platforms, self.coins_manager.coins, touches
            )

            # Dessin
            self.const.SCREEN.fill((255, 255, 255))
            self.const.SCREEN.blit(self.resized_background, (0, 0))

            # Si le jeu est pausé (Fin de jeu)
            if self.is_paused:
                self.pause_iteration += 1
                self.pause_inputs = True
                if self.pause_iteration >= self.const.FPS:
                    self.const.CLOCK.tick(self.const.FPS)
                    self.platform_manager.draw_platforms()
                    self.coins_manager.draw_coins()
                    if self.gameover:
                        self.const.SCREEN.blit(text, text_rect)
                    if self.gamewon:
                        self.const.SCREEN.blit(text_win, text_win_rect)
                    self.const.SCREEN.blit(text2, text2_rect)
                    self.const.SCREEN.blit(text_coin, text_coin_rect)
                    self.player.draw()
                    pg.display.flip()
                    continue

            self.coins_manager.draw_coins()
            self.player.draw()

            # Montrer le compteur de pièces
            self.const.SCREEN.blit(text_coin, text_coin_rect)
            self.coins_manager.text_coin = [
                pg.Rect(
                        text_coin_rect.left - self.const.COIN_WIDTH - 10,
                        text_coin_rect.top + text_coin_rect.height/2 - self.const.COIN_HEIGHT/2,
                        self.const.COIN_WIDTH,
                        self.const.COIN_HEIGHT,
                        )
                ]


            # Système de génération des platformes et des pièces.

            if len(platforms) == 1:
                for i in range(3):
                    self.platform_manager.gen_platform(platforms[i])

            if self.player.current_platform_index > len(platforms) - 3:
                self.platform_manager.gen_platform(platforms[len(platforms)-1])

            self.platform_manager.draw_platforms()
            self.coins_manager.add_coins(platforms, self.coins_manager.coins)

            # Défilement vertical
            def scrolling(self, offset=None):
                if self.player.y < self.const.HEIGHT // 3:
                    if offset is None:
                        offset = self.const.HEIGHT // 3 - self.player.y
                    self.player.y += offset
                    self.scrolling_to_reverse.append(offset)
                    for platform in self.platform_manager.platforms:
                        platform.y += offset
                    for coin in self.coins_manager.coins:
                        coin.y += offset
            
            scrolling(self)

            if self.player.check_if_gameover():

                self.const.SCREEN.blit(text, text_rect)
                self.const.SCREEN.blit(text2, text2_rect)
                self.is_paused = True
                self.gameover = True

            # Montrer le texte du jeu gagné
            if self.player.coins_counter >= self.const.WIN_COINS:
                self.const.SCREEN.blit(text_win, text_win_rect)
                self.const.SCREEN.blit(text2, text2_rect)
                self.is_paused = True
                self.gamewon = True
            

            # Rafraîchissement
            pg.display.flip()
            self.const.CLOCK.tick(self.const.FPS)
        else:
            pg.quit()
            sys.exit()
