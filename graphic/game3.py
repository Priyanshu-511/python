import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.Font(None, 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = GREEN
        self.radius = 20  # 2 cm radius
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = BLUE
        self.radius = 20  # 2 cm radius
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.rect.y = random.randint(-100, -50)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = GOLD
        self.radius = 5  # Bullet radius
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# Boss class
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = RED
        self.radius = 35  #3.5 cm radius
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.x = SCREEN_WIDTH // 2 - self.radius
        self.rect.y = -200
        self.speed_y = 2
        self.attack_delay = 60
        self.attack_counter = 0
        self.health = 5

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 0:
            self.speed_y = 0
        self.attack_counter += 1
        if self.attack_counter >= self.attack_delay:
            self.attack_counter = 0
            self.attack()

    def attack(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Variables
score = 0
health = 5
boss_spawned = False

# Game level
level = 1
enemy_spawn_rate = 0.01  # Initial spawn rate

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_SPACE:
                player.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # Spawn enemies with adjusted frequency
    if random.random() < enemy_spawn_rate:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Check for collisions between bullets and enemies
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10
        if score % 500 == 0:
            level += 1
            enemy_spawn_rate += 0.000005  # Increase spawn rate with each level

    # Check for collisions between player and enemies
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        health -= 1

    # Check if boss should spawn
    if score >= level * 150 and not boss_spawned:
        boss = Boss()
        all_sprites.add(boss)
        boss_spawned = True

    # Check for collisions between bullets and boss
    if boss_spawned:
        hits = pygame.sprite.groupcollide([boss], bullets, False, True)
        for hit in hits:
            boss.health -= 1
            if boss.health <= 0:
                score += 100
                boss.kill()
                boss_spawned = False
                level += 1
                enemy_spawn_rate += 0.05  # Increase spawn rate with each boss defeat

    # Update sprites
    all_sprites.update()

    # Clear the screen
    screen.fill(WHITE)

    # Draw sprites
    for sprite in all_sprites:
        pygame.draw.circle(screen, sprite.color, sprite.rect.center, sprite.radius)

    # Draw text
    score_text = font.render("Score: " + str(score), True, GREEN)
    screen.blit(score_text, (10, 10))
    health_text = font.render("Health: " + str(health), True, RED)
    screen.blit(health_text, (10, 50))
    level_text = font.render("Level: " + str(level), True, BLUE)
    screen.blit(level_text, (10, 90))

    # Update the display
    pygame.display.flip()

    # Check for game over
    if health <= 0:
        running = False

    # Control frame rate
    clock.tick(60)

# Game over text
game_over_text = font.render("Game Over", True, RED)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
pygame.display.flip()

# Delay before quitting
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
