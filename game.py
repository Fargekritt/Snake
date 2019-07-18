import random

import pygame

import snake
import cube

width = 500
height = width
rows = 20

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake")


def draw_grid(w, rows, surface):
    size = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x += size
        y += size

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    surface.fill((0, 0, 0))
    s.draw(surface)
    draw_grid(width, rows, surface)
    snack.draw(surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)


def main():
    global s, snack
    clock = pygame.time.Clock()
    s = snake.Snake((255, 0, 0), (10, 10), looping=False)
    snack = cube.Cube(random_snack(rows, s), color=(0, 255, 0))
    run = True
    while run:
        keys = pygame.key.get_pressed()
        clock.tick(10)
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for key in keys:
            if keys[pygame.K_a]:
                s.add_cube()
                break
        if s.body[0].pos == snack.pos:
            s.add_cube(snack.color)
            r = random.randrange(255)
            g = random.randrange(255)
            b = random.randrange(255)
            snack = cube.Cube(random_snack(rows, s), color=(r, g, b))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))
                s.reset((10, 10))
                break
        if s.head.pos[0] < 0 or s.head.pos[0] > rows - 1 or s.head.pos[1] < 0 or s.head.pos[1] > rows - 1:
            s.reset((10, 10))
        s.move()
        redraw_window(win)
    pygame.quit()


if __name__ == "__main__":
    main()
