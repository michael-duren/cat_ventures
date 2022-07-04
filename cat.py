import pygame

class Cat:
    """A class to manage the cat character."""

    def __init__(self, cv_game):
        """Initialize the cat and set it's starting position"""
        self.screen = cv_game.screen
        self.screen_rect = cv_game.screen.get_rect()

        # Load the cat image and get it's rect.
        self.image = pygame.image.load('/Users/michaelduren/Desktop/Video Games/pictures/cat.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the cat at its current location"""
        self.screen.blit(self.image, self.rect)