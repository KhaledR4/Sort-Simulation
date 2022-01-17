from photos.Hero.characters import character_surf_up, character_surf_right, character_surf_left, character_surf_down
from Constants import av_width, av_height
import pygame as py


class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img_index = 0
        self.image = character_surf_right[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.health = 100

    def move_next_step(self, pos1, pos2):
        '''
        Moves the character from position 1 to position 2
        The two positions should be neighbors
        :param pos1: coordinates (tuple) of the initial position
        :param pos2: coordinates (tuple) of the final position
        :return: None while the character is moving
                 False when the character reaches the final position
        '''
        if pos1[1] == pos2[1]:
            if pos2[0] == pos1[0]+1:  # move right
                if self.rect.topleft[0] < pos2[0]*av_width:
                    self.rect.left += 1
                    self.img_index += 1
                    if self.img_index == 9:
                        self.img_index = 0
                    self.image = character_surf_right[self.img_index]
                else:
                    return False
            if pos2[0] == pos1[0] - 1:  # move left
                if self.rect.topleft[0] > pos2[0] * av_width:
                    self.rect.left -= 1
                    self.img_index += 1
                    if self.img_index == 9:
                        self.img_index = 0
                    self.image = character_surf_left[self.img_index]
                else:
                    return False
        if pos1[0] == pos2[0]:
            if pos2[1] == pos1[1] + 1:  # move down
                if self.rect.topleft[1] < pos2[1] * av_height:
                    self.rect.top += 1
                    self.img_index += 1
                    if self.img_index == 9:
                        self.img_index = 0
                    self.image = character_surf_down[self.img_index]
                else:
                    return False
            if pos2[1] == pos1[1] - 1:  # move up
                if self.rect.topleft[1] > pos2[1] * av_height:
                    self.rect.top -= 1
                    self.img_index += 1
                    if self.img_index == 9:
                        self.img_index = 0
                    self.image = character_surf_up[self.img_index]
                else:
                    return False
