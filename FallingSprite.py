"""
FallingSprite class for the Finite Jumper game.
Represents a sprite that falls and rotates as an obstacle or effect.
"""

import pygame

class FallingSprite:
    """
    Represents a falling and rotating sprite in the game.
    """
    def __init__(self, screen, x, y):
        """
        Initializes the falling sprite's properties.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = 0
        self.image = pygame.image.load("assets/down.png")

    def rotate(self):
        """
        Rotates the sprite image.
        """
        self.angle += 10
        if self.angle >= 360:
            self.angle = 0
        self.image = pygame.transform.rotate(pygame.image.load("assets/down.png"), self.angle)

    def draw(self):
        """
        Draws the falling sprite on the screen.
        """
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        """
        Updates the sprite's position and rotation. Returns True if it should be deleted.
        """
        self.rotate()
        if self.y >= 720:
            return True
        return False

    def delete(self):
        """
        Deletes the sprite's data.
        """
        self.image = None
        self.x = None
        self.y = None
        self.angle = None
        self.screen = None