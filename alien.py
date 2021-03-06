import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the Aliens exact position
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        # draw the ship at its current location

        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True