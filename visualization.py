import sys
import pygame
import typing as t
import time
from util import list_remap


SIZE = WIDTH, HEIGHT = 800, 350

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

MINIMUM_LINE_LENGTH = 50
SEPARATION = 8

TICK_RATE = 10


def draw_lines(
    screen: pygame.Surface,
    main_color: t.Tuple[int, int, int],
    checking_color: t.Tuple[int, int, int],
    known_color: t.Tuple[int, int, int],
    LIST: t.List[t.Union[int, float]],
    checking: t.List[int],
    known: t.List[int]
) -> t.List[pygame.Rect]:
    """Draw lines with every lines length corresponding to the value from list."""
    LIST = list_remap(LIST, (0, HEIGHT - MINIMUM_LINE_LENGTH))
    lines = []

    for index, value in enumerate(LIST):
        # Start with 20 units gap, and draw lines with SEPARATION units separation on X
        x_pos = 20 + index * SEPARATION
        # Get height on Y axis
        y_pos = HEIGHT - value - MINIMUM_LINE_LENGTH
        # Draw lines in `checking` and `known` with contrasting color
        if index in checking:
            color = checking_color
        elif index in known:
            color = known_color
        else:
            color = main_color

        # Draw the lines and add them into `lines` list
        line = pygame.draw.line(screen, color, (x_pos, HEIGHT), (x_pos, round(y_pos)))
        lines.append(line)

    return lines


def main_loop(screen: pygame.Surface, fps_clock: pygame.time.Clock, LIST: t.List[int]) -> None:
    """Main loop which preforms bubble sort and visualizes the process"""
    for m in range(1, len(LIST)):
        for i in range(len(LIST) - m):
            # Handle user quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Get 2 comparing elements on `i` and `i + 1`
            element_1 = LIST[i]
            element_2 = LIST[i + 1]

            # Reset the screen and redraw lines with `i` and `i + 1` as contrasting
            screen.fill(BLACK)
            draw_lines(screen, WHITE, RED, GREEN, LIST, [i, i + 1], list(range(len(LIST) - m + 1, len(LIST))))

            # Update the screen and wait for tick
            pygame.display.update()
            fps_clock.tick(TICK_RATE)

            # Check if elements needs to be swapped
            if element_1 > element_2:
                # Swap the elements in list
                LIST[i] = element_2
                LIST[i + 1] = element_1

                # Reset the screen and redraw swapped lines (and highlight them)
                screen.fill(BLACK)
                draw_lines(screen, WHITE, RED, GREEN, LIST, [i, i + 1], list(range(len(LIST) - m + 1, len(LIST))))

                # Update the screen and wait for tick
                pygame.display.update()
                fps_clock.tick(TICK_RATE)


def pygame_start(LIST: t.List[int]) -> None:
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    fps_clock = pygame.time.Clock()

    # Don't start straight away
    time.sleep(3)

    main_loop(screen, fps_clock, LIST)

    # Don't close right away
    time.sleep(3)


LIST = [12, 58, 21, 13, 18, 42, 35, 49, 10, 3, 50, 28, 55, 1, 8, 3, 24, 49]

pygame_start(LIST)
