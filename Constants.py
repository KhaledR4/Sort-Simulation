from Functions import Draw
from photos.Hero.characters import character_surf_right
import pygame as py

WIDTH = 800
HEIGHT = 400
av_width = Draw.average_size(character_surf_right)[0]
av_height = Draw.average_size(character_surf_right)[1]
screen = py.display.set_mode((WIDTH, HEIGHT))
spots = []
for i in range(int(WIDTH/av_width)):
    for j in range(int(HEIGHT/av_height)):
        spots.append((i, j))
