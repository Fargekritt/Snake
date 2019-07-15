import pygame

import snake

width = 500
height = width
rows = 20


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
    pygame.display.update()


def random_snack(rows, item):
    pass


def main():
    global s
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("snake")

    s = snake.Snake((255, 0, 0), (10, 10))
    run = True
    while run:
        keys = pygame.key.get_pressed()
        pygame.time.delay(100)
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for key in keys:
            if keys[pygame.K_a]:
                s.add_cube()
                break
        s.move()
        redraw_window(win)
    pygame.quit()


if __name__ == "__main__":
    main()
