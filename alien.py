import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to control the alien oppressors"""

    def __init__(self, ai_game):
        """Initialize the alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien's position
        self.x = float(self.rect.x)