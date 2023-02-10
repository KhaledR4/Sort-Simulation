import pygame as py
from constants import *
from Sort_algos import *

# initialize pygame settings
py.init()
clock = py.time.Clock()
#########

header_buttons = [
        Button(40, 10, "Sort", sort_button_function, colors["grey"], True),
        Button(200, 10, 'Search', search_button_function, colors["white"], True),
]
sort_buttons = [
    Button(20, 80, "Basic", basic_sort, colors["white"], False),
    Button(100, 80, "Bubble", bubble_sort, colors["white"], False),
    Button(180, 80, "Insert", insertion_sort, colors["white"], False),
    Button(260, 80, "Quick", quick_sort, colors["white"], False),
    Button(340, 80, "Count", counting_sort, colors["white"], False),
    Button(420, 80, "Bucket", bucket_sort, colors["white"], False),
    Button(500, 80, "Merge", merge, colors["white"], False),
]
Main_Page = Screen(header_buttons, sort_buttons, header_buttons)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if py.mouse.get_pressed()[0]:
            x, y = py.mouse.get_pos()
            Main_Page.check_collision((x, y))
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                Main_Page.reset()
    screen.fill('White')
    Main_Page.draw()
    py.display.update()
    clock.tick(60)
