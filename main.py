import pygame
import math

pygame.init()

width, height = 800, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spiral Circle")

colorBall = (255, 255, 0)
black = (0, 0, 0)

angle = 0
radius = 0
center_x, center_y = width // 2, height // 2
speed = 0.05
radius_increase = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    x = center_x + int(math.cos(angle) * radius)
    y = center_y + int(math.sin(angle) * radius)

    pygame.draw.circle(screen, colorBall, (x, y), 10)

    angle += speed
    radius += radius_increase

    pygame.display.flip()
    clock.tick(60)
    pygame.time.delay(10)

pygame.quit()
