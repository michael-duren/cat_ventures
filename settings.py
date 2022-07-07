class Settings:
    """A Class to store all settings for Cat Ventures"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 204, 255)

        # Meow settings
        self.meow_speed = 1.0
        self.meow_width = 3
        self.meow_height = 15
        self.meow_color = (0, 0, 0)
        self.meows_allowed = 3

        # Cat settings
        self.cat_speed = 1.5