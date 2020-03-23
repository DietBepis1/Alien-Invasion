import pygame
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.score = 0

        #Font settings and color information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        #Prepare the initial score and level images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    
    def prep_score(self):
        """Turn the score into a rendered image"""

        #Unused code for Python Crash Course's arcade scoring
        #but I didn't like this method.
        #rounded_score = round(self.stats.score, -1)
        #score_str = str(self.stats.score)

        score_str = "Score: {:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Display the score at the top-right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores and ships to the screen"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    

    def prep_high_score(self):
        """Turn the high score into a rendered image"""

        high_score_str = "Hi Score: {:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        

        #Highscore placed at top-left of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    
    def check_high_score(self):
        """Check if there is a new high score"""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """Turn the level number into a rendered image"""

        level_str = "Level: {}".format(self.stats.level)
        self.level_image = self.font.render(level_str, 1, self.text_color, self.settings.bg_color)
        
        #Position the level in the center
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 1

    
    def prep_ships(self):
        """Show how many ships are left"""

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
