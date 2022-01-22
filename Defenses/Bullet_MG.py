import pygame as py
from Constants import av_height, av_width
import math
from Functions.Algo import relative_pos
bullets = [py.image.load("photos/PNG_cannon/Bullet_MG.png")]


class Bullet_MG(py.sprite.Sprite):
    def __init__(self, x, y, target):
        super().__init__()
        self.image_index = 0
        self.image = bullets[self.image_index]
        self.image = py.transform.scale(self.image, (av_width, av_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.target = target

    def get_slope(self):
        dalta_y = self.rect.centery-self.target.rect.centery
        dalta_x = self.rect.centerx-self.target.rect.centerx
        if dalta_x != 0:
            return abs(dalta_y/dalta_x)
        else:
            return -1

    def update(self, group):
        x, y = relative_pos(self.rect.center, self.target.rect.center)
        if self.target.rect.colliderect(self.rect):
            group.remove(self)
            return 0
        slope = round(self.get_slope(), 1)
        self.image = py.transform.rotate(bullets[self.image_index], math.degrees(math.atan(y/x)))
        self.image = py.transform.scale(self.image, (av_width / 3, av_height / 3))
        if self.rect.centerx < self.target.rect.centerx:
            self.rect.centerx += 3
        else:
            self.rect.centerx -= 3
        if self.rect.centery < self.target.rect.centery:
            self.rect.centery += 3*slope
        else:
            self.rect.centery -= 3*slope
