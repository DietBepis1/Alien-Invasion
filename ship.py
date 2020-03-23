import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship! XD"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load teh ship and get its rect
        self.image = pygame.image.load('images/poop.bmp')
        self.rect = self.image.get_rect()

        #Starting pos of ship is at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store ship's positions as a float
        self.x = float(self.rect.x)
        
        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

    
    def center_ship(self):
        """Center ship at midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    