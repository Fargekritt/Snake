import pygame

import snake

width = 500
height = 500
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
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    pass


def main():
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("snake")

    s = snake.Snake((255, 0, 0), (10, 10))

    run = True
    while run:
        pygame.time.delay(100)
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    s.move("left")
                elif keys[pygame.K_RIGHT]:
                    s.move("right")
                elif keys[pygame.K_UP]:
                    s.move("up")
                elif keys[pygame.K_DOWN]:
                    s.move("down")
    pygame.quit()


if __name__ == "__main__":
    main()
