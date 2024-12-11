import pygame as pg
from constantes import Constantes
from platforms import PlatformsManager
from random import randint


class CoinsManager:
    def __init__(self):
        self.const = Constantes()
        self.platforms = PlatformsManager().platforms

        self.coins = []
        self.text_coin = []
        self.already_cycled = []


        for i in range(1, len(self.platforms)):
            # On fait attention à ne pas ajouter de pièces sur toutes les platformes
            platform = self.platforms[i]
            if platform in self.already_cycled:
                return
            else:
                self.already_cycled.append(platform)

            if randint(0, 1) == 1:
                self.coins.append(
                    pg.Rect(
                        platform.left + platform.width / 2 - self.const.COIN_WIDTH / 2,
                        platform.top - platform.height - 10,
                        self.const.COIN_WIDTH,
                        self.const.COIN_HEIGHT,
                    )
                )

    def draw_coins(self):
        if len(self.text_coin) > 0:
            pg.draw.rect(self.const.SCREEN, self.const.YELLOW, self.text_coin[0])

        for coins in self.coins:
            pg.draw.rect(self.const.SCREEN, self.const.YELLOW, coins)
