import pygame

class Ship():
    #initilize ship and set starting position

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        #load image and get its rect
        self.image = pygame.image.load('space_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #position ship on screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ships position based on movement flag
        if self.moving_right:
            self.center += self.settings.ship_speed_factor
        #if instead of elif so both can be used at once
        if self.moving_left:
            self.center -= self.settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)
