import pygame as py
from sys import exit
from Functions import Draw
from photos.Hero.characters import character_surf_right
from Constants import av_width, av_height, WIDTH, HEIGHT, screen, spots
from Functions import Algo
from Player.Player_class import Player
from Defenses.Cannon import Cannon
from Defenses.MG import MG_defense

py.init()
clock = py.time.Clock()
Hero = Player(0, 0)
Hero_group = py.sprite.Group()
Hero_group.add(Hero)
Cannon_group = py.sprite.Group()
cannons = []
Bullet_group = py.sprite.Group()
Bullet_MG_group = py.sprite.Group()
MG_list = []
MG_group = py.sprite.Group()
rectangles = []
path = []
moving = False
index = 0
shoot = 0
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                moving = True
        if py.mouse.get_pressed()[0]:
            x, y = py.mouse.get_pos()
            x = int(x/av_width)
            y = int(y/av_height)
            if (x, y) not in rectangles:
                rectangles.append((x, y))
        if py.mouse.get_pressed()[2]:
            x, y = py.mouse.get_pos()
            x = int(x/av_width)
            y = int(y/av_height)
            MG_deployed = MG_defense(x*av_width, y*av_height, py.time.get_ticks())
            MG_group.add(MG_deployed)
            MG_list.append(MG_deployed)
        if py.mouse.get_pressed()[1]:
            x, y = py.mouse.get_pos()
            x = int(x/av_width)
            y = int(y/av_height)
            Cannon_deployed = Cannon(x*av_width, y*av_height, py.time.get_ticks())
            Cannon_group.add(Cannon_deployed)
            cannons.append(Cannon_deployed)
    screen.fill('Black')
    Draw.draw_grid(screen=screen, images=character_surf_right, height=HEIGHT, width=WIDTH)
    Draw.draw_rectangles(screen=screen, rectangles=rectangles, av_width=av_width, av_height=av_height)
    Hero_group.draw(screen)
    Cannon_group.draw(screen)
    MG_group.draw(screen)
    Bullet_group.draw(screen)
    Bullet_MG_group.draw(screen)
    Bullet_MG_group.update(Bullet_MG_group)
    Bullet_group.update(Bullet_group)
    if moving:
        path = Algo.algorithm((0, 0), (10, 4), rectangles, spots)
        moving = False
    if path:
        check = Hero.move_next_step(path[index], path[index + 1])
        if check == False and index != (len(path) - 2):
            index += 1
    if cannons:
        for cannon in cannons:
            if cannon.target is None:
                cannon.closest_target([Hero])
            else:
                cannon.check_target_availability()
                cannon.shoot(Bullet_group, py.time.get_ticks())
    if MG_list:
        for MG in MG_list:
            if MG.target is None:
                MG.closest_target([Hero])
            else:
                MG.check_target_availability()
                MG.shoot(Bullet_MG_group, py.time.get_ticks())
    py.display.update()
    clock.tick(60)
