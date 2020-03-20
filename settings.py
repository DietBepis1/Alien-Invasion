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
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (33, 112, 51)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents rightward movement, -1 to the left
        self.fleet_direction = 1





    