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
    first_color = (0, 255, 0)
    second_color = (0, 0, 255)
    clock = pygame.time.Clock()
    s = snake.Snake((255, 0, 0), (10, 10), looping=False)
    snack = cube.Cube(random_snack(rows, s), color=first_color)
    game_state = "run"
    game_tick = 10

    while game_state == "run":
        keys = pygame.key.get_pressed()
        clock.tick(game_tick)
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = "quit"

        for key in keys:
            # press "a" to add cubes
            if keys[pygame.K_a]:
                s.add_cube((255, 0, 0), average=True)
                break
            if keys[pygame.K_p]:
                game_state = "pause"

        # if head is on snack add cube and make new snack
        if s.body[0].pos == snack.pos:
            s.add_cube(snack.color)
            if (len(s.body) % 10) < 5:
                color = first_color
            else:
                color = second_color
            snack = cube.Cube(random_snack(rows, s), color = color, random_color=False)
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))
                s.reset((10, 10))
                break
        # lose cond
        if s.head.pos[0] < 0 or s.head.pos[0] > rows - 1 or s.head.pos[1] < 0 or s.head.pos[1] > rows - 1:
            print('Score: ', len(s.body))
            s.reset((10, 10))
        s.move()
        redraw_window(win)
    pygame.quit()


if __name__ == "__main__":
    main()
