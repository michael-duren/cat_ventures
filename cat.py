import pygame

class Cat:
    """A class to manage the cat character."""

    def __init__(self, cv_game):
        """Initialize the cat and set it's starting position"""
        self.screen = cv_game.screen
        self.settings = cv_game.settings
        self.screen_rect = cv_game.screen.get_rect()

        # Load the cat image and get it's rect.
        self.image = pygame.image.load('/Users/michaelduren/Desktop/Video Games/pictures/cat.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the cats horizontal position.
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the cats position based on the movement flag."""
        # Update the cat's x value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.cat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.cat_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the cat at its current location"""
        self.screen.blit(self.image, self.rect)