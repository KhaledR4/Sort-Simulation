import pygame as py
import random

py.init()
key_font = py.font.Font(py.font.get_default_font(), 12)
axis_font = py.font.Font(py.font.get_default_font(), 9)
font = py.font.Font(py.font.get_default_font(), 16)
header_font = py.font.Font(py.font.get_default_font(), 24)
screen_size = 800
screen = py.display.set_mode((screen_size, screen_size))
bars = 64
max_height = 600     # Change to 25 to try count sort
total_width = int(screen_size/bars)
bar_width = int(0.9*total_width)
space_btwn_bars = int(0.1*total_width)
colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "grey": (105, 105, 105)
}


def search_button_function(page):
    page.set_method_search()


def sort_button_function(page):
    page.set_method_sort()
