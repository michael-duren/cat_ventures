import pygame
from pygame.sprite import Sprite

class Meow(Sprite):
    """A class to manage meows fired from the cat"""

    def __init__(self, cv_game):
        """Create a meow object at the cat's current position."""
        super().__init__()
        self.screen = cv_game.screen
        self.settings = cv_game.settings
        self.color = self.settings.meow.color

        # Create a meow rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, self.settings.meow_width,
        self.settings.meow_height)
        self.rect.midtop = cv_game.cat.rect.midtop

        # Store the meows position as a decimal value, 
        self.y = float(self.rect.y)

    def update(self):
        """Move the meow up the screen."""
        # Update the decimal position of the meow.
        self.y -= self.settings.meow_speed
        self.rect.y = self.y

    def draw_meow(self):
        """Draw the meow to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)