import pygame as py
from Constants import av_height, av_width
import math
from Functions.Algo import relative_pos
bullets = [py.image.load("photos/PNG_cannon/Bullet_MG.png")]
for i in range(len(bullets)):
    bullets[i] = py.transform.scale(bullets[i], (av_width/3, av_height/3))


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
        dalta_y = self.rect.centery - self.target.rect.centery
        dalta_x = self.rect.centerx - self.target.rect.centerx
        if dalta_x == 0:
            return 100
        slope = abs(dalta_y / dalta_x)
        if slope < 20:
            return slope
        else:
            return 100

    def update(self, group):
        # destroy if collided
        if self.target.rect.colliderect(self.rect):
            group.remove(self)
            self.target.health -= 25
            return 0

        # rotate and move the bullet
        x, y = relative_pos(self.rect.center, self.target.rect.center)
        same_horizontal_line = False
        slope = self.get_slope()
        if slope != 100:
            slope = round(slope, 1)
            if slope < 0.2:
                same_horizontal_line = True
                if self.rect.centerx > self.target.rect.centerx:
                    self.image = py.transform.rotate(bullets[self.image_index], 90)

                else:
                    self.image = py.transform.rotate(bullets[self.image_index], -90)
            else:
                self.image = py.transform.rotate(bullets[self.image_index], math.degrees(math.atan(y / x)))
            if self.rect.centerx < self.target.rect.centerx:
                self.rect.centerx += 3
            else:
                self.rect.centerx -= 3
            if self.rect.centery < self.target.rect.centery and not same_horizontal_line:
                self.image = py.transform.rotate(self.image, 180)
                self.rect.centery += 3 * slope
            else:
                self.rect.centery -= 3 * slope
        else:
            if self.rect.centery > self.target.rect.centery:
                self.rect.centery -= 3
            else:
                self.image = py.transform.rotate(bullets[self.image_index], 180)
                self.rect.centery += 3
