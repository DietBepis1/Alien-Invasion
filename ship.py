import pygame

class Ship:
    """A class to manage teh spacezoomer XD"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load teh ship and get its rect
        self.image = pygame.image.load('images/poop.bmp')
        self.rect = self.image.get_rect()

        #Starting pos of ship is at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)