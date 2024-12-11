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

    def add_coins(self, platforms, coins):
        for platform in platforms:
            if platform in self.already_cycled:
                continue
            self.already_cycled.append(platform)
    
            if randint(0, 1) == 1:
                coin = pg.Rect(
                    platform.left + platform.width / 2 - self.const.COIN_WIDTH / 2,
                    platform.top - self.const.COIN_HEIGHT - self.const.COIN_PLATFORM_MARGIN,
                    self.const.COIN_WIDTH,
                    self.const.COIN_HEIGHT,
                )
                coins.append(coin)


    def draw_coins(self):
        if len(self.text_coin) > 0:
            pg.draw.rect(self.const.SCREEN, self.const.YELLOW, self.text_coin[0], border_radius=3)

        for coins in self.coins:
            pg.draw.rect(self.const.SCREEN, self.const.YELLOW, coins, border_radius=3)
