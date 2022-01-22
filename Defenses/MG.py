from Constants import av_height, av_width
import pygame as py
from Functions.Algo import distance
from Defenses.Bullet_MG import Bullet_MG
MG_photo = [py.image.load("photos/PNG_cannon/MG.png").convert_alpha()]


class MG_defense(py.sprite.Sprite):
    def __init__(self, x, y, time):
        super().__init__()
        self.image_index = 0
        self.image = MG_photo[self.image_index]
        self.image = py.transform.scale(self.image, (av_width, av_height))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.range = 2000
        self.target = None
        self.time = time
        self.time_btwn_hits = 3000

    def closest_target(self, players):
        minimum = self.range
        for player in players:
            d = distance(self.rect.center, player.rect.center)
            if d < minimum:
                minimum = d
                self.target = player

    def check_target_availability(self):
        if (distance(self.rect.center, self.target.rect.center) < self.range) and (self.target.health != 0):
            pass
        else:
            self.target = None

    def shoot(self, group, instant):
        if (instant - self.time) > self.time_btwn_hits:
            group.add(Bullet_MG(self.rect.centerx, self.rect.centery, self.target))
            self.time = instant
