import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    #initialize game and create screen object
    pygame.init()
    #instance of settings and ship
    settings = Settings()

    #accessing attributes of Settings from the instance
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen, settings)

    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, settings, ship)
        pygame.display.flip()

run_game()
