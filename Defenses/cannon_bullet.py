import pygame as py
from Constants import av_height, av_width

bullets = [py.image.load("photos/PNG_cannon/Bullet_Cannon.png")]


class Bullet(py.sprite.Sprite):
    def __init__(self, x, y, target):
        super().__init__()
        self.image_index = 0
        self.image = bullets[self.image_index]
        self.image = py.transform.scale(self.image, (av_width/3, av_height/3))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.target = target

    def update(self, *args, **kwargs):
        self.rect.centerx += 1
