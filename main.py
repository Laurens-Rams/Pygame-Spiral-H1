import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spiral Circle")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Spiral parameters
angle = 0
radius = 0
center_x, center_y = width // 2, height // 2
speed = 0.1
radius_increase = 0.5
directionVar = 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(black)

    # Calculate new position
    x = center_x + int(math.cos(angle) * radius)
    y = center_y + int(math.sin(angle) * radius)

    # Check for horizontal boundaries and reverse direction if needed
    if player_pos.x > screen.get_width()//2 - 15 or player_pos.x < 15:
        directionVar = -directionVar

    # Update the position of the circle
    player_pos = pygame.Vector2(x, y)
    pygame.draw.circle(screen, white, player_pos, 15)

    # Update the angle and radius
    angle += speed
    radius += radius_increase

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
