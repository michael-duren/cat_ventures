import sys

from settings import Settings

from cat import Cat

import pygame

class CatVentures:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cat Ventures meow")

        self.cat = Cat(self)

    def run_game(self):
        """Start with the main game loop"""
        while True:
            self._check_events()
            self.cat.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.cat.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.cat.moving_right = False

    def _update_screen(self):
        """Update images on the screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.cat.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    cv = CatVentures()
    cv.run_game()