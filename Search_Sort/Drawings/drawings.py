from constants import *
import pygame as py


def draw_one_bar(bar, color, secondary=False):
    bar.color = colors[color]
    bar.draw(secondary)
    py.display.update()


def draw_count_table(count_list, current_number=None, cumulative=[]):
    py.draw.rect(screen, colors["white"], (0, 135, 800, 85))
    if current_number is not None:
        py.draw.line(screen, colors["black"], start_pos=(30 * current_number + 95, 135), end_pos=(30 * current_number +
                                                                                                  95, 155))
        py.draw.line(screen, colors["black"], start_pos=(30 * current_number + 90, 145), end_pos=(30 * current_number +
                                                                                                  95, 155))
        py.draw.line(screen, colors["black"], start_pos=(30 * current_number + 100, 145), end_pos=(30 * current_number +
                                                                                                  95, 155))
    text_surface = font.render('height', True, (0, 0, 0))
    screen.blit(text_surface, (5, 160))
    text_surface = font.render('count', True, (0, 0, 0))
    screen.blit(text_surface, (5, 180))
    if cumulative:
        py.draw.line(screen, colors["black"], start_pos=(0, 194), end_pos=(1000, 194))
        text_surface = font.render('cumulative', True, (0, 0, 0))
        screen.blit(text_surface, (2, 200))
    py.draw.line(screen, colors["black"], start_pos=(0, 175), end_pos=(1000, 175))

    for i in range(len(count_list)):
        py.draw.line(screen, colors["black"], start_pos=(30 * i + 90, 155), end_pos=(30 * i + 90, 215))
        text_surface_1 = font.render(str(i), True, (0, 0, 0))
        screen.blit(text_surface_1, (30*i + 93, 160))
        text_surface_2 = font.render(str(count_list[i]), True, (0, 0, 0))
        screen.blit(text_surface_2, (30 * i + 93, 180))
        if cumulative:
            text_surface_3 = font.render(str(cumulative[i]), True, (0, 0, 0))
            screen.blit(text_surface_3, (30 * i + 93, 200))
    py.display.update()


def draw_bucket_representation(buckets):
    current_length = 0
    for i, bucket in enumerate(buckets):
        line_height = screen_size - 100 * i - 120
        line_start_x = current_length
        current_length += len(bucket) * total_width
        line_end_x = current_length
        py.draw.line(screen, colors["black"], start_pos=(line_start_x, line_height),
                     end_pos=(line_end_x, line_height))
        py.draw.line(screen, colors["black"], start_pos=(line_start_x, line_height),
                     end_pos=(line_start_x+10, line_height+10))
        py.draw.line(screen, colors["black"], start_pos=(line_start_x, line_height),
                     end_pos=(line_start_x + 10, line_height - 10))
        py.draw.line(screen, colors["black"], start_pos=(line_end_x, line_height),
                     end_pos=(line_end_x - 10, line_height + 10))
        py.draw.line(screen, colors["black"], start_pos=(line_end_x, line_height),
                     end_pos=(line_end_x - 10, line_height - 10))
        text = font.render(f'{i*100}-{(i+1)*100-1}', True, (0, 0, 0))
        surface = text.get_rect()
        surface.bottomleft = (line_start_x + 0.3*(line_end_x-line_start_x), line_height)
        screen.blit(text, surface)

    py.display.update()
