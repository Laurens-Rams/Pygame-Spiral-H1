import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
directionVar = 1
circle_radius = 40  # Set the radius of the circle

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for horizontal boundaries and reverse direction if needed
    if player_pos.x > screen.get_width() - circle_radius or player_pos.x < circle_radius:
        directionVar = -directionVar

    # Update the position of the circle
    player_pos += pygame.Vector2(10 * directionVar, 0)

    # Fill the screen with a color to wipe away anything from the last frame
    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, circle_radius)

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
