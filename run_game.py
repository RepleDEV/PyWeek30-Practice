import pygame
import math
import time

pygame.font.init()

WINDOW_SIZE = (800, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("#1")

running = True

deg1 = 0
deg2 = 1

CIRCLEWIDTH = 10

autoSpin = True

while running:
    pygame.time.delay(8)
    # clock.tick(60)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not autoSpin:
        deg1 += 1
        deg2 += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                autoSpin = not autoSpin
        if event.type == pygame.QUIT:
            running = False
            break
    WINDOW.fill((255,255,255))

    if autoSpin:
        deg1 += 1
        deg2 += 1

    sin = round(math.sin(math.radians(deg1)) * 100)
    cos = round(math.cos(math.radians(deg2)) * 100)

    centerY = round(WINDOW_SIZE[1] / 2 - CIRCLEWIDTH / 2)
    centerX = int(round(WINDOW_SIZE[0] / 2 - CIRCLEWIDTH / 2))

    pygame.draw.circle(WINDOW, (255,0,0), (centerX, sin + centerY), CIRCLEWIDTH)
    pygame.draw.circle(WINDOW, (0,255,0), (cos + centerX, centerY), CIRCLEWIDTH)
    # print(round(math.sin(math.radians(deg)) * 100))
    pygame.display.update()

pygame.exit()