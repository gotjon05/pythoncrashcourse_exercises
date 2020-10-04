import sys
import pygame 



from settings import Settings

def run_game():
    #initialize game and create screen object 
    pygame.init()

    #instance of settings -- instantiation 
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
   
    while True:

        screen.fill(settings.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

run_game() 
