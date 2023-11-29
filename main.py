import pygame
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spiral Circle")

white = (255, 255, 255)
black = (0, 0, 0)

angle = 0
radius = 0
center_x, center_y = width // 2, height // 2
speed = 0.1
radius_increase = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    x = center_x + int(math.cos(angle) * radius)
    y = center_y + int(math.sin(angle) * radius)

    pygame.draw.circle(screen, white, (x, y), 15)
    pygame.draw.line(screen, white, (center_x, center_y), (x, y))

    if radius > screen.get_height() // 2 or radius < 0:
        radius_increase = -radius_increase

    angle += speed
    radius += radius_increase
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()