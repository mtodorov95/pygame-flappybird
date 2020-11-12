import pygame
import sys
import os

base_dir = os.getcwd()
game_dir = os.path.join(base_dir, 'game')
assets_dir = os.path.join(game_dir, 'assets')

pygame.init()

screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load(os.path.join(
    assets_dir, 'background-day.png')).convert()
bg_surface = pygame.transform.scale2x(bg_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    pygame.display.update()
    clock.tick(120)
