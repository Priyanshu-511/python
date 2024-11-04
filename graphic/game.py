import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
PLAYER_SIZE = 50
PLAYER_COLOR = RED
PLAYER_VELOCITY = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

clock = pygame.time.Clock()

# Player rectangle
player_rect = pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_SIZE // 2, SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_VELOCITY
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_VELOCITY

    # Keep player within screen bounds
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - PLAYER_SIZE))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - PLAYER_SIZE))

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player rectangle
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
