import pygame as py
from sys import exit
from Functions import Draw
from photos.Hero.characters import character_surf_right
from Constants import av_width, av_height, WIDTH, HEIGHT, screen
from Player.Player_class import Player
from Defenses.Cannon import Cannon
from Defenses.MG import MG_defense

py.init()
clock = py.time.Clock()
Hero = Player(av_width, av_height)
Hero_2 = Player(av_width, av_height*2)
Hero_group = py.sprite.Group()
Hero_group.add(Hero)
Heroes = [Hero]
Cannon_group = py.sprite.Group()
cannons = []
Bullet_group = py.sprite.Group()
Bullet_MG_group = py.sprite.Group()
MG_list = []
MG_group = py.sprite.Group()
rectangles = []

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
        if py.mouse.get_pressed()[1]:
            x, y = py.mouse.get_pos()
            x = int(x/av_width)
            y = int(y/av_height)
            player_deployed = Player(x*av_width, y*av_height)
            Hero_group.add(player_deployed)
            Heroes.append(player_deployed)
        if py.mouse.get_pressed()[2]:
            x, y = py.mouse.get_pos()
            x = int(x/av_width)
            y = int(y/av_height)
            Cannon_deployed = Cannon(x*av_width, y*av_height, py.time.get_ticks())
            Cannon_group.add(Cannon_deployed)
            cannons.append(Cannon_deployed)
    screen.fill('Green')
    Draw.draw_grid(screen=screen, images=character_surf_right, height=HEIGHT, width=WIDTH)
    Draw.draw_rectangles(screen=screen, rectangles=rectangles, av_width=av_width, av_height=av_height)
    Hero_group.draw(screen)
    Hero_group.update(screen, Hero_group, Heroes, cannons + MG_list, rectangles, py.time.get_ticks())
    Cannon_group.draw(screen)
    Cannon_group.update(screen, Bullet_group, Heroes, Cannon_group, cannons)
    MG_group.draw(screen)
    MG_group.update(screen, Bullet_MG_group, Heroes, MG_group, MG_list)
    Bullet_group.draw(screen)
    Bullet_MG_group.draw(screen)
    Bullet_MG_group.update(Bullet_MG_group)
    Bullet_group.update(Bullet_group)
    py.display.update()
    clock.tick(60)
