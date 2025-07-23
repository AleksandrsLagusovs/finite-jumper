"""
Ground class for the Finite Jumper game.
Represents the ground platform at the bottom of the screen.
"""

import pygame

class Ground():
    """
    Represents the ground platform in the game.
    """
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 720-20
        self.width = 1280
        self.height = 20
        self.color = (255, 255, 255)

    def draw(self):
        """
        Draws the ground on the screen.
        """
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))