class GameStats:
    """Track stats for the game"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        
        #start the game in an inactive state
        self.game_active = False

        #Record high scores but never reset them
        self.high_score = 0

    
    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
