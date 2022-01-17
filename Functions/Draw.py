import pygame as py


def average_size(images):
    '''
    finds the average size of a list of images.
    used for grid drawing
    :param images: list of png images
    :return: tuple of average width and height of the images
    '''
    height = 0
    width = 0
    for image in images:
        width += image.get_size()[0]
        height += image.get_size()[1]
    width = int(width/len(images))
    height = int(height/len(images))
    return width, height


def draw_grid(screen, images, height, width):
    '''
    Draws a grid with spacing equal to the average width and height of the images
    :param screen: surface to draw on
    :param images: list of images used to find the average width and height
    :param height: int height
    :param width: int width
    '''
    horizontal_lines = int(height/average_size(images)[1])+1
    vertical_lines = int(width/average_size(images)[0])+1
    pos_y = 0
    pos_x = 0
    for i in range(horizontal_lines):
        py.draw.line(screen, color='Black', start_pos=(0, pos_y), end_pos=(width, pos_y))
        pos_y += int(average_size(images)[1])
    for i in range(vertical_lines):
        py.draw.line(screen, color="Black", start_pos=(pos_x, 0), end_pos=(pos_x, height))
        pos_x += int(average_size(images)[0])


def draw_rectangles(screen, rectangles, av_width, av_height):
    '''
    Draws rectangles with the average width and height of images
    :param screen: surface to draw on
    :param rectangles: list of tuples of the positions of each rectangle
    :param av_width: average width of the character
    :param av_height: average height of the character
    '''
    for rectangle in rectangles:
        py.draw.rect(screen, color="Green", rect=(rectangle[0]*av_width, rectangle[1]*av_height, av_width, av_height))
