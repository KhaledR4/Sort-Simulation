from Constants import av_height, av_width
import pygame as py
from Functions.Algo import distance, relative_pos
from Defenses.cannon_bullet import Bullet
import math

cannons = [py.image.load("photos/PNG_cannon/Cannon.png").convert_alpha()]
for i in range(len(cannons)):
    cannons[i] = py.transform.scale(cannons[i], (av_width, av_height))


class Cannon(py.sprite.Sprite):
    def __init__(self, x, y, time):
        super().__init__()
        self.image_index = 0
        self.pos = (x/av_width, y/av_height)
        self.image = cannons[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.range = 2000
        self.target = None
        self.time = time
        self.time_btwn_hits = 3000
        self.health = 100

    def closest_target(self, players):
        '''
        Finds the closest player and if found sets it as the object target
        :param players: list of all the players
        '''
        minimum = self.range
        for player in players:
            d = distance(self.rect.center, player.rect.center)
            if d < minimum:
                minimum = d
                self.target = player

    def check_target_availability(self):
        '''
        Checks if the targeted player is still alive and still in range
        '''
        if (distance(self.rect.center, self.target.rect.center) < self.range) and (self.target.health > 0):
            return True
        else:
            self.target = None
            return False

    def shoot(self, group, instant):
        '''
        Shoots the target
        :param group: group of bullets
        :param instant: time of each frame
        '''
        if (instant - self.time) > self.time_btwn_hits:
            group.add(Bullet(self.rect.centerx, self.rect.centery, self.target))
            self.time = instant

    def update(self, screen, bullet_group, players, cannon_group, cannon_list):
        '''
        :param screen: surface to draw on
        :param bullet_group: group of bullets
        :param players: list of all the players to be used to check closest target
        :param cannon_group: group of cannons
        :param cannon_list: list of all cannons
        '''
        # draw health bar
        length = av_width
        py.draw.line(screen, 'Grey', (self.rect.left, self.rect.top - 4), (self.rect.right, self.rect.top - 4), 4)
        py.draw.line(screen, 'Red', (self.rect.left, self.rect.top - 4),
                     (self.rect.left + (self.health / 100) * length,
                      self.rect.top - 4), 4)

        # check the target or find new one and rotate towards it
        if self.target is not None:
            x, y = relative_pos(self.rect.center, self.target.rect.center)
            if x != 0:
                self.image = py.transform.rotate(cannons[self.image_index], math.degrees(math.atan(y / x)))
            if self.rect.centery < self.target.rect.centery:
                self.image = py.transform.rotate(self.image, 180)
            if self.check_target_availability():
                self.shoot(bullet_group, py.time.get_ticks())
        else:
            self.closest_target(players)

        # checks if dead
        if self.health <= 0:
            index = 0
            cannon_group.remove(self)
            for cannon in cannon_list:
                if self.rect.center == cannon.rect.center:
                    del cannon_list[index]
                    break
                else:
                    index += 1
            return 0
