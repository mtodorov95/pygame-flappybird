import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

# Variables
base_dir = os.getcwd()
game_dir = os.path.join(base_dir, 'game')
assets_dir = os.path.join(game_dir, 'assets')

gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load(os.path.join(
    assets_dir, 'background-day.png')).convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load(
    os.path.join(assets_dir, 'base.png')).convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load(
    os.path.join(assets_dir, 'bluebird-midflap.png')).convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, 512))


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12

    screen.blit(bg_surface, (0, 0))
    bird_movement += gravity
    bird_rect.centery += bird_movement

    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
