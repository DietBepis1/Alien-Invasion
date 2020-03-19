import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    
    def _check_events(self):
        """Respond to kb/m presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        """Handles screen refreshing"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        #Make most recently drawn screen visible
        pygame.display.flip()
        
    
    def run_game(self):
        """Start game loop"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    #make game instance

    ai = AlienInvasion()
    ai.run_game()