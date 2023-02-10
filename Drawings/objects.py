from constants import *
import pygame as py


class Key:
    def __init__(self, x, y, color, text):
        self.color = color
        self.text = key_font.render(text, True, (0, 0, 0))
        self.x = x
        self.y = y

    def draw(self):
        py.draw.rect(screen, self.color, (self.x, self.y, 20, 20))
        surface = self.text.get_rect()
        surface.topleft = (self.x+30, self.y+5)
        screen.blit(self.text, surface)


class DrawLegends:
    @staticmethod
    def basic_sort():
        key_1 = Key(20, 120, colors["red"], "Current Minimum")
        key_2 = Key(20, 150, colors["green"], "To Compare")
        key_1.draw()
        key_2.draw()
        py.display.update()

    @staticmethod
    def bubble_sort():
        key_1 = Key(20, 120, colors["red"], "Current Index")
        key_2 = Key(20, 150, colors["green"], "Index Before Current One")
        key_1.draw()
        key_2.draw()
        py.display.update()

    @staticmethod
    def insertion_sort():
        key_1 = Key(20, 120, colors["red"], "Current Index")
        key_2 = Key(20, 150, colors["green"], "Index Before Current One")
        key_3 = Key(20, 180, colors["black"], "Break as all to the left are smaller")
        key_1.draw()
        key_2.draw()
        key_3.draw()
        py.display.update()

    @staticmethod
    def quick_sort():
        key_1 = Key(20, 120, colors["red"], "Pivot")
        key_2 = Key(20, 150, colors["green"], "Current Index")
        key_3 = Key(20, 180, colors["black"], "To Compare")
        key_1.draw()
        key_2.draw()
        key_3.draw()
        py.display.update()

    @staticmethod
    def merge_sort():
        key_1 = Key(20, 120, colors["red"], "Left SubArray")
        key_2 = Key(20, 150, colors["green"], "Right SubArray")
        key_1.draw()
        key_2.draw()


class Bar:
    def __init__(self, height, index):
        self.height = height
        self.color = colors["blue"]
        self.index = index

    def x_position(self):
        return self.index * total_width

    def draw(self, secondary=False):
        if not secondary:
            if max_height > 70:
                py.draw.rect(screen, self.color, (self.x_position(), screen_size-self.height, bar_width, self.height))
            else:
                py.draw.rect(screen, self.color, (self.x_position(), screen_size - self.height*10, bar_width, self.height*10))
        else:
            if max_height > 70:
                py.draw.rect(screen, self.color, (self.x_position(), screen_size*0.6-self.height, bar_width, self.height))
            else:
                py.draw.rect(screen, self.color, (self.x_position(), screen_size*0.6 - self.height * 10, bar_width, self.height * 10))
                index_text = axis_font.render(str(self.index), True, (0, 0, 0))
                screen.blit(index_text, (self.x_position(), screen_size*0.6+15))


class Button:
    def __init__(self, x, y, text, on_press=None, color=colors["white"], header=False):
        self.x = x
        self.y = y
        self.isHeader = header
        self.font = header_font if header else font
        self.height = 30 if header else 20
        self.width = 100 if header else 70
        self.text = self.font.render(text, True, (0, 0, 0))
        self.color = color
        self.surface = self.text.get_rect()
        self.surface.topleft = (self.x, self.y)
        self.function = on_press

    def draw(self):
        py.draw.rect(screen, self.color, (self.x - 0.1*self.surface.width, self.y - 0.1*self.surface.height,
                                          self.width, self.height),  border_radius=10)
        py.draw.rect(screen, colors["black"],
                     (self.x - 0.1 * self.surface.width, self.y - 0.1 * self.surface.height, self.width,
                      self.height), 1,  border_radius=10)
        screen.blit(self.text, self.surface)

    def on_press(self, page):
        self.color = colors["grey"]
        self.draw()
        py.display.update()
        if not self.isHeader:
            self.function(page.to_sort)
        else:
            self.function(page)


class Screen:
    def __init__(self, main_buttons, sort_buttons, search_buttons):
        self.to_sort = [Bar(random.randrange(1, max_height), i) for i in range(bars)]
        self.sort_buttons = sort_buttons
        self.main_buttons = main_buttons
        self.search_buttons = search_buttons
        self.method = "Sort"

    def set_method_search(self):
        self.method = "Search"

    def set_method_sort(self):
        self.method = "Sort"

    def reset(self):
        self.to_sort = [Bar(random.randrange(1, max_height), i) for i in range(bars)]

    def draw(self):
        for element in self.to_sort:
            element.draw()
        if self.method == "Sort":
            for button in self.sort_buttons:
                button.draw()
        else:
            for button in self.search_buttons:
                button.draw()
        for button in self.main_buttons:
            button.draw()
        py.draw.line(screen, colors["grey"], start_pos=(0, 70), end_pos=(700, 70))

    def reset_colors(self, buttons):
        for button in buttons:
            button.color = colors["white"]

    def check_collision(self, position):
        if self.method == "Sort":
            for button in self.sort_buttons:
                if button.surface.collidepoint(position):
                    self.reset_colors(self.sort_buttons)
                    button.on_press(self)
        for button in self.main_buttons:
            if button.surface.collidepoint(position):
                self.reset_colors(self.main_buttons)
                button.on_press(self)
