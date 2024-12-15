import pygame as pg
from platforms import PlatformsManager
from constantes import Constantes
from sprite import Sprite

# Classe Joueur
class Player:
    def __init__(self):
        self.platform_manager = PlatformsManager()
        self.const = Constantes()
        self.width = 50
        self.height = 50
        self.coins_counter = 0

        # Placer le joueur sur la première plateforme
        starting_platform = self.platform_manager.platforms[0]  # Choisir la première plateforme
        self.current_platform_index = 0
        self.original_x = starting_platform.left + (starting_platform.width - self.width) // 2
        self.original_y = starting_platform.top - self.height
        self.x = starting_platform.left + (starting_platform.width - self.width) // 2  # Centré horizontalement
        self.y = starting_platform.top - self.height  # Juste au-dessus de la plateforme 
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 0.5 
        self.on_ground = True

        # Création d'une instance du joueur
        self.sprites = Sprite()

        # Groupe de sprites (facilite le rendu et les collisions)
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.sprites)
    
    def check_if_gameover(self):
        if self.y > pg.display.Info().current_h:
            return True
        else:
            return False
        
    def check_if_won(self):
        if self.coins_counter >= self.const.WIN_COINS:
            return True
        else:
            return False
        

    def handle_input(self):
        keys = pg.key.get_pressed()

        if (keys[pg.K_RETURN] or keys[pg.K_KP_ENTER]) and (self.check_if_gameover() or self.check_if_won()):
            self.x = self.original_x
            self.y = self.original_y
            self.velocity_y = 0
            self.on_ground = True
            self.coins_counter = 0
            

        # Si le jeu est pausé, on ignore tous les inputs (Sauf entrée).
        if self.check_if_gameover() or self.check_if_won():
            return

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

    def check_collision(self, platforms, coins):
        self.on_ground = False
        for platform in platforms:
            if (
                self.y + self.height >= platform.top
                and self.y + self.height <= platform.bottom
                and self.x + self.width > platform.left
                and self.x < platform.right
            ):
                self.y = platform.top - self.height
                self.velocity_y = 0
                self.on_ground = True
                self.current_platform_index = platforms.index(platform)
        for coin in coins:
            if (
                self.x < coin.x + coin.width and
                self.x + self.width > coin.x and
                self.y < coin.y + coin.height and
                self.y + self.height > coin.y
            ):
                coins.remove(coin)
                self.coins_counter += 1

    def update(self, platforms, coins, touches):
        self.handle_input()
        self.apply_gravity()
        self.check_collision(platforms, coins)
        self.sprites.active_sprite(touches, self.on_ground, self.speed, self.x, self.y)

    def draw(self):
        self.all_sprites.draw(self.const.SCREEN)
        #pg.draw.rect(self.const.SCREEN, self.const.BLACK, (self.x, self.y, self.width, self.height), border_radius=3)
