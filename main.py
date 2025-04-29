import pygame
import random

# Inicializálás
pygame.init()

# Képernyő beállítások
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egyszerű Platformer Játék")

# Betöltés
player_img = pygame.image.load("assets/player.png")
platform_img = pygame.image.load("assets/platform.png")
bg_color = (135, 206, 250)

# Játékos adatok
player = pygame.Rect(100, 500, 50, 50)
player_vel_y = 0
gravity = 0.5
jump_power = -10
on_ground = False

# Platformok
platforms = [pygame.Rect(100, 550, 200, 20),
             pygame.Rect(400, 400, 200, 20),
             pygame.Rect(200, 300, 200, 20)]

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
score = 0


def draw_window():
    win.fill(bg_color)
    win.blit(player_img, (player.x, player.y))
    for plat in platforms:
        win.blit(platform_img, (plat.x, plat.y))
    score_text = font.render(f"Pont: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))
    pygame.display.update()


# Fő ciklus
run = True
while run:
    clock.tick(60)
    player_vel_y += gravity
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    player.y += player_vel_y
    on_ground = False
    for plat in platforms:
        if player.colliderect(plat) and player_vel_y > 0:
            player.y = plat.y - player.height
            player_vel_y = 0
            on_ground = True
            score += 1

    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_power

    # Ha leesik
    if player.y > HEIGHT:
        print("Vége a játéknak!")
        run = False

    draw_window()

pygame.quit()
