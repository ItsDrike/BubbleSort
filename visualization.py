import sys
import pygame
import time
from util import list_remap
from collections import defaultdict


class Colors:
    """This class is only used to store colors."""
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    ORANGE = 255, 165, 0


ARRAY = [12, 58, 21, 13, 18, 42, 35, 49, 10, 3, 50, 28, 55, 1, 8, 3, 24, 49]
STATES = defaultdict(lambda: Colors.WHITE)


def bubble_sort(game: "Game") -> None:
    """
    Use bubble sort algorithm to sort any given list of
    numbers or floats, this is being done in O(n^2).
    """
    for m in range(1, len(ARRAY)):
        for i in range(len(ARRAY) - m):
            # Pick 2 elements and compare them
            # if first element is higher, swap them, else keep them
            if ARRAY[i] > ARRAY[i + 1]:
                # These lines are being swapped
                STATES[i] = Colors.RED
                STATES[i + 1] = Colors.RED

                ARRAY[i], ARRAY[i + 1] = ARRAY[i + 1], ARRAY[i]
            else:
                # These lines won't be swapped
                STATES[i] = Colors.BLUE
                STATES[i + 1] = Colors.BLUE

            # Update game window
            game.update_screen()

            # Reset the line colors
            STATES[i] = Colors.WHITE
            STATES[i + 1] = Colors.WHITE
        # This line is already correctly sorted
        STATES[len(ARRAY) - m] = Colors.GREEN


class Game:
    # How far are individual lines from each other
    SEPARATION = 8
    # How fast should the tick rate be
    TICK_RATE = 10
    # Set window parameters
    SIZE = WIDTH, HEIGHT = 400, 350

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        self.fps_clock = pygame.time.Clock()

    def handle_user_quit(self) -> None:
        """If user quits, exit the game and stop program."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def redraw_screen(self) -> None:
        """
        Redraw all lines on the screen.

        This does not update the screen, it only redraws it.
        """
        # Reset screen to black
        self.screen.fill(Colors.BLACK)

        # Map values from array onto pygame window height
        arr = list_remap(ARRAY, (0, Game.HEIGHT))

        # Draw individual lines
        for index, value in enumerate(arr):
            # Round the value before working with it
            # This is necessary because pygame doesn't accept floats
            value = round(value)

            # Start with 10 units gap, draw lines with given separation between them
            x_pos = 10 + index * Game.SEPARATION
            # Subtract the value from height, pygame is inverted on Y axis
            y_pos = Game.HEIGHT - value

            pos1 = (x_pos, Game.HEIGHT)
            pos2 = (x_pos, y_pos)

            color = STATES[index]

            pygame.draw.line(self.screen, color, pos1, pos2)

    def update_screen(self, tick: bool = True) -> None:
        """
        Update the screen accordingly to `redraw_screen`
        also check for user quit and tick (until specified otherwise).
        """
        self.handle_user_quit()
        self.redraw_screen()

        # Update the display and tick when needed
        pygame.display.update()
        if tick:
            self.fps_clock.tick(Game.TICK_RATE)


game = Game()
# Starting timeout
time.sleep(3)

bubble_sort(game)
game.update_screen()

# Don't stop straight away
time.sleep(3)
