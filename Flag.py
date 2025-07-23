"""
Flag class for the Finite Jumper game.
Represents the goal flag that the player must reach.
"""

import pygame

class Flag:
    """
    Represents the flag object in the game.
    """
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 25
        self.height = 40
        self.image = pygame.image.load("assets/flag.png")
        self.captured = False

    def draw(self):
        """
        Draws the flag on the screen if it has not been captured.
        """
        if not self.captured:
            self.screen.blit(self.image, (self.x, self.y))