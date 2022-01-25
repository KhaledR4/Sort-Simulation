from photos.Hero.characters import character_surf_up, character_surf_right, character_surf_left
from photos.Hero.characters import character_surf_down, character_died
from Constants import av_width, av_height, spots
import pygame as py
from Functions.Algo import distance, get_neighbors, algorithm


class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img_index = 0
        self.image = character_surf_right[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.health = 100
        self.target = None
        self.searching = True
        self.path = []
        self.index = 0
        self.dead_index = 0
        self.die_time_animation = 100
        self.time = 0
        self.attack_pos = False

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

    def closest_target(self, defenses):
        '''
        Finds the closest defense to attack and sets it as the target of the player
        :param defenses: list of all deployed defenses
        '''
        minimum = 1000
        for defense in defenses:
            d = distance(self.rect.center, defense.rect.center)
            if d < minimum:
                minimum = d
                self.target = defense

    def check_target_availability(self):
        '''
        Checks if the targeted defense is still alive
        '''
        if self.target.health > 0:
            return True
        else:
            self.target = None
            return False

    def position_to_move(self, barriers):
        '''
        Finds the closest neighbor to the targeted defense
        :param barriers: list of all the position of the obstacles. The position is given as a tuple of row and column
        :return: the closest neighbor
        '''
        if self.target is not None:
            neighbors = get_neighbors(self.target.pos, barriers)
            minimum = 1000
            best = None
            for neighbor in neighbors:
                d = distance(self.rect.center, (neighbor[0]*av_width, neighbor[1]*av_height))
                if d < minimum:
                    minimum = d
                    best = neighbor
            return best

    def update(self, screen, group, players, defenses, barriers, time):
        '''
        checks if the player is dead and removes it from the group and list of players
        :param screen: surface to draw health bar on
        :param group: pygame group having all player sprites
        :param players: list of player sprites
        :param defenses: list of all defenses
        :param barriers: list of all the position of the obstacles. The position is given as a tuple of row and column
        :param time: time at each frame
        '''

        # draw health bar
        length = av_width
        py.draw.line(screen, 'Grey', (self.rect.left, self.rect.top - 4), (self.rect.right, self.rect.top - 4), 4)
        py.draw.line(screen, 'Blue', (self.rect.left, self.rect.top - 4), (self.rect.left + (self.health/100)*length,
                                                                           self.rect.top-4), 4)
        # check if dead
        if self.health <= 0:
            self.image = character_died[self.dead_index]
            if time - self.time > self.die_time_animation:
                self.dead_index += 1
                self.time = time
            if self.dead_index == 5:
                i = 0
                group.remove(self)
                for player in players:
                    if self.rect.center == player.rect.center:
                        del players[i]
                        break
                    else:
                        i += 1
                return 0

        # check target
        if self.target is not None:
            check = False
            if self.check_target_availability():
                if self.searching:
                    self.path = algorithm((round(self.rect.left/av_width), round(self.rect.top/av_height)),
                                          self.position_to_move(barriers), barriers, spots)
                    self.searching = False
                    print(self.path)
                if self.path:
                    if self.index < len(self.path) - 1:
                        check = self.move_next_step(self.path[self.index], self.path[self.index + 1])
                    else:
                        # print("Reached target")
                        # print(self.rect.topleft[0]/av_width, self.rect.topleft[1]/av_height)
                        self.index = 0
                        self.path = []
                        self.attack_pos = True
                    if check == False:
                        self.index += 1
                if self.attack_pos:
                    self.target.health -= 1
            else:
                self.target = None
                self.attack_pos = False
                self.searching = True
        else:
            self.closest_target(defenses)
