import pygame

import cube


class Snake():
    body = []
    turns = {}

    def __init__(self, color, pos, looping=False):
        self.color = color
        self.head = cube.Cube(pos)
        self.body.append(self.head)
        self.pos = pos
        self.looping = looping

        self.dirnx = 0
        self.dirny = 0

    def move(self):
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if self.looping:
                    if c.dirnx == -1 and c.pos[0] <= 0:
                        c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                        c.pos = (0, c.pos[1])
                    elif c.dirny == -1 and c.pos[1] <= 0:
                        c.pos = (c.pos[0], c.rows-1)
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                        c.pos = (c.pos[0], 0)
                    else:
                        c.move(c.dirnx, c.dirny)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube.Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 0

    def add_cube(self, cube_color):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(
                cube.Cube((tail.pos[0]-1, tail.pos[1]), cube_color))
        elif dx == -1 and dy == 0:
            self.body.append(
                cube.Cube((tail.pos[0]+1, tail.pos[1]), cube_color))
        elif dx == 0 and dy == 1:
            self.body.append(
                cube.Cube((tail.pos[0], tail.pos[1]-1), cube_color))
        elif dx == 0 and dy == -1:
            self.body.append(
                cube.Cube((tail.pos[0], tail.pos[1]+1), cube_color))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
