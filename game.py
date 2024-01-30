import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

# Player
player_radius = 25
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Bullets
bullets = []
bullet_speed = 10
last_shoot_time = 0
shoot_delay = 500  # Half a second in milliseconds

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    if current_time - last_shoot_time >= shoot_delay:
        if keys[pygame.K_SPACE]:
            # Shoot a bullet in the direction of the mouse cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.degrees(math.atan2(mouse_y - player_y, mouse_x - player_x))

            bullet = {
                "x": player_x,
                "y": player_y,
                "angle": angle,
            }
            bullets.append(bullet)
            last_shoot_time = current_time

    # Update bullet positions
    for bullet in bullets:
        bullet["y"] -= bullet_speed * math.sin(math.radians(bullet["angle"]))
        bullet["x"] -= bullet_speed * math.cos(math.radians(bullet["angle"]))

    # Remove bullets that go off-screen
    bullets = [bullet for bullet in bullets if 0 <= bullet["x"] < WIDTH and 0 <= bullet["y"] < HEIGHT]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (player_x, player_y), player_radius)

    for bullet in bullets:
        pygame.draw.circle(screen, RED, (int(bullet["x"]), int(bullet["y"]), 5))

    pygame.display.update()

    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
