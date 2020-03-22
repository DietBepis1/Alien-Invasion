class Settings:
    """A class to store settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""

        #Screen settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 8
        self.bullet_height = 5
        self.bullet_color = (33, 112, 51)
        self.bullets_allowed = 5

        #alien settings
        self.fleet_drop_speed = 7
        

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the settings that will change as the game progresses"""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1

        #fleet_direction of 1 represents rightward movement, -1 to the left
        self.fleet_direction = 1
        


    def increase_speed(self):
        """Increase speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale





    