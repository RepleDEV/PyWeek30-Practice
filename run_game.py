import pygame
import math

pygame.font.init()

WINDOW_SIZE = (800, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("#1")

done = False

color = (0, 128, 255)

is_blue = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:
            done = True

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    pygame.draw.rect(WINDOW, color, (30, 30, 60, 60))

    pygame.display.flip()