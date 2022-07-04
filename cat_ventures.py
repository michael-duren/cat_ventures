import sys, pygame

from settings import Settings

from cat import Cat

from meow import Meow
class CatVentures:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cat Ventures meow")

        self.cat = Cat(self)
        self.meows = pygame.sprite.Group()

    def run_game(self):
        """Start with the main game loop"""
        while True:
            self._check_events()
            self.cat.update()
            self.meows.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_meow()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = False

    def _fire_meow(self):
        """Create a new meow and add it to the meows group."""
        new_meow = Meow(self)
        self.meows.add(new_meow)

    def _update_screen(self):
        """Update images on the screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.cat.blitme()
        for meow in self.meows.sprites():
            meow.draw_meow()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    cv = CatVentures()
    cv.run_game()