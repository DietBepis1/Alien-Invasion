import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class for ammunition management"""

    def __init__(self, ai_game):
        """Create a bullet FROM THIN AIR!"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        #Update position of bullet
        self.y -= self.settings.bullet_speed
        #Update rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
