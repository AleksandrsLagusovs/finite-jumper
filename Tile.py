"""
Tile class for the Finite Jumper game.
Represents a platform tile that the jumper can land on.
"""

import pygame

class Tile:
    """
    Represents a platform tile in the game.
    """
    last_id = 0

    def __init__(self, screen, x, y, x_velocity, max_displacement=0):
        """
        Initializes the tile's properties.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.max_displacement = max_displacement
        self.displacement = 0
        self.x_velocity = x_velocity
        self.width = 100
        self.height = 10
        self.color = (255, 255, 255)
        self.id = Tile.last_id
        Tile.last_id += 1
        # self.text_surface = self.pre_render_text() # uncomment to display tile numbers for debugging

    def pre_render_text(self):
        """
        Pre-renders the tile's ID as a text surface (for debugging).
        """
        font = pygame.font.Font(None, 28)
        text_surface = font.render(str(self.id), True, (255, 255, 255))
        return text_surface

    def draw(self):
        """
        Draws the tile on the screen.
        """
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), border_radius=10)
        # self.screen.blit(self.text_surface, (self.x-20, self.y-20)) # uncomment to display tile numbers for debugging

    def __str__(self):
        """
        Returns a string representation of the tile.
        """
        return f"tile {self.id} at ({self.x}, {self.y})"