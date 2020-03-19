class Settings:
    """A class to store settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (33, 112, 51)
        self.bullets_allowed = 5



    