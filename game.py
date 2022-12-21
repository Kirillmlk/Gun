import pygame
import control
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Score



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space War")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    control.create_army(screen, inos)
    stats = Stats()
    sc = Score(screen, stats)

    while True:
        control.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gan()
            bullets.update()
            control.update(bg_color, screen, stats, sc, gun, inos, bullets)
            control.update_bullets(screen, stats, sc, inos, bullets)
            control.update_inos(stats, screen, sc, gun, inos, bullets)


run()