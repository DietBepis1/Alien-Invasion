import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start game loop"""

        while True:
            #Watch for kb/m events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #redraw the screen during each pass of loop
            self.screen.fill(self.settings.bg_color)
            
            #Make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    #make game instance

    ai = AlienInvasion()
    ai.run_game()