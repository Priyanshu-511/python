import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = RED
PLAYER_VELOCITY = 7
PLAYER_GRAVITY = 0.3
PLAYER_JUMP_VELOCITY = -10
PLAYER_MAX_JUMP = 10  # Maximum height the player can jump

# Enemy properties
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_COLOR = BLUE
ENEMY_VELOCITY = 5

# Coin properties
COIN_WIDTH = 30
COIN_HEIGHT = 30
COIN_COLOR = YELLOW

# Platform properties
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = BLUE

# Bullet properties
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_COLOR = BLACK
BULLET_VELOCITY = 10

# Scoring and Health
SCORE = 0
HEALTH = 3

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumping = False

    def update(self):
        self.gravity()
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def gravity(self):
        if self.velocity_y == 0:
            self.velocity_y = 1
        else:
            self.velocity_y += PLAYER_GRAVITY

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.velocity_y >= 0:
            self.velocity_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.velocity_y = PLAYER_JUMP_VELOCITY
            self.jumping = True

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += ENEMY_VELOCITY * self.direction
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - ENEMY_WIDTH:
            self.direction *= -1

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((COIN_WIDTH, COIN_HEIGHT))
        self.image.fill(COIN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += BULLET_VELOCITY
        if self.rect.left > SCREEN_WIDTH:
            self.kill()  # Remove the bullet when it goes off-screen

# Create sprites groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
platform = Platform(0, SCREEN_HEIGHT - PLATFORM_HEIGHT)
platforms.add(platform)
all_sprites.add(platform)
platform = Platform(SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2, SCREEN_HEIGHT // 2)
platforms.add(platform)
all_sprites.add(platform)
platform = Platform(SCREEN_WIDTH - PLATFORM_WIDTH, SCREEN_HEIGHT - PLATFORM_HEIGHT)
platforms.add(platform)
all_sprites.add(platform)

# Create enemies
enemy = Enemy(100, SCREEN_HEIGHT - PLATFORM_HEIGHT - ENEMY_HEIGHT)
enemies.add(enemy)
all_sprites.add(enemy)
enemy = Enemy(500, SCREEN_HEIGHT - PLATFORM_HEIGHT - ENEMY_HEIGHT)
enemies.add(enemy)
all_sprites.add(enemy)

# Create coins
coin = Coin(200, SCREEN_HEIGHT - PLATFORM_HEIGHT - COIN_HEIGHT - 50)
coins.add(coin)
all_sprites.add(coin)
coin = Coin(600, SCREEN_HEIGHT - PLATFORM_HEIGHT - COIN_HEIGHT - 100)
coins.add(coin)
all_sprites.add(coin)

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.right, player.rect.centery - BULLET_HEIGHT // 2)
                all_sprites.add(bullet)
                bullets.add(bullet)
            elif event.key == pygame.K_UP:  # Additional key to jump
                player.jump()

    # Handle player movement
    keys = pygame.key.get_pressed()
    player.velocity_x = 0
    if keys[pygame.K_LEFT]:
        player.velocity_x = -PLAYER_VELOCITY
    if keys[pygame.K_RIGHT]:
        player.velocity_x = PLAYER_VELOCITY

    # Update player
    player.update()

    # Check for collisions with platforms
    collision = pygame.sprite.spritecollide(player, platforms, False)
    if collision:
        player.rect.y = collision[0].rect.top
        player.velocity_y = 0

    # Check for collisions with enemies
    enemy_collision = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for enemy_hit in enemy_collision:
        enemy = Enemy(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH), random.randint(0, SCREEN_HEIGHT - ENEMY_HEIGHT))
        enemies.add(enemy)
        all_sprites.add(enemy)
        SCORE += 10

    # Check for collisions with coins
    coin_collision = pygame.sprite.spritecollide(player, coins, True)
    if coin_collision:
        SCORE += 10

    # Update enemies
    enemies.update()

    # Update bullets
    bullets.update()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Draw text
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(score_text, (10, 10))
    health_text = font.render(f"Health: {HEALTH}", True, BLACK)
    screen.blit(health_text, (SCREEN_WIDTH - 150, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
