import random

import pygame
from game import width, rows


class Cube():

    def __init__(self, start, dirnx=0, dirny=0, color=(255, 0, 0), random_color=False):
        self.pos = start
        self.dirnx = 0
        self.dirny = 0
        if random_color:
            self.r = random.randrange(255)
            self.g = random.randrange(255)
            self.b = random.randrange(255)
            self.color = (self.r, self.g, self.b)
        else:
            self.color = color
        self.width = width
        self.rows = rows

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color,
                         (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        if eyes:  # Draws the eyes
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
