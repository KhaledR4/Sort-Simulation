import pygame as py


screen = py.display.set_mode((800, 400))
character_surf_right = [py.image.load("photos/Hero/Walk_right/walk1.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk2.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk3.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk4.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk5.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk6.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk7.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk8.png").convert_alpha(),
                        py.image.load("photos/Hero/Walk_right/walk9.png").convert_alpha(), ]

character_surf_left = [py.image.load("photos/Hero/Walk_left/walk1.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk2.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk3.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk4.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk5.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk6.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk7.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk8.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_left/walk9.png").convert_alpha(), ]

character_surf_up = [py.image.load("photos/Hero/Walk_up/walk1.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk2.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk3.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk4.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk5.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk6.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk7.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk8.png").convert_alpha(),
                     py.image.load("photos/Hero/Walk_up/walk9.png").convert_alpha(), ]

character_surf_down = [py.image.load("photos/Hero/Walk_down/walk1.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk2.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk3.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk4.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk5.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk6.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk7.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk8.png").convert_alpha(),
                       py.image.load("photos/Hero/Walk_down/walk9.png").convert_alpha(), ]

character_died = [py.image.load("photos/Hero/Die/die1.png").convert_alpha(),
                  py.image.load("photos/Hero/Die/die2.png").convert_alpha(),
                  py.image.load("photos/Hero/Die/die3.png").convert_alpha(),
                  py.image.load("photos/Hero/Die/die4.png").convert_alpha(),
                  py.image.load("photos/Hero/Die/die5.png").convert_alpha()]
