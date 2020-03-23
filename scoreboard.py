import pygame

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes"""
        
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.score = 0

        #Font settings and color information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score images
        self.prep_score()
        self.prep_high_score()

    
    def prep_score(self):
        """Turn the score into a rendered image"""

        #Unused code for Python Crash Course's arcade scoring
        #but I didn't like this method.
        #rounded_score = round(self.stats.score, -1)
        #score_str = str(self.stats.score)

        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        #Display the score at the top-right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen"""

        self.screen.blit(self.score_image, self.score_rect)
    

    def prep_high_score(self):
        """Turn the high score into a rendered image"""

        self.high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(self.high_score_str, True, self.text_color, self.settings.bg_color)
        

        #Highscore placed at top-left of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = 20