import pygame

class Ship():
    #initilize ship and set starting position


    def __init__(self, screen):
        self.screen = screen

        #load image and get its rect
        self.image = pygame.image.load('space_ship.bmp')
        self.rect = self.image.get_rect()

        #position ship on screen 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #draw ship at current location 
        self.screen.blit(self.image, self.rect)
