from Constants import av_height, av_width
import pygame as py
from Functions.Algo import distance
from Defenses.cannon_bullet import Bullet
from Player.Player_class import Player

cannons = [py.image.load("photos/PNG_cannon/Cannon.png")]


class Cannon(py.sprite.Sprite):
    def __init__(self, x, y, range, time):
        super().__init__()
        self.image_index = 0
        self.image = cannons[self.image_index]
        self.image = py.transform.scale(self.image, (av_width, av_height))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.range = range
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
        if (distance(self.rect.center,self.target.rect.center)< self.range) and (self.target.health != 0):
            pass
        else:
            self.target = None

    def shoot(self, group, instant):
        if (instant - self.time) > self.time_btwn_hits:
            group.add(Bullet(self.rect.centerx, self.rect.centery, self.target))
            self.time = instant
