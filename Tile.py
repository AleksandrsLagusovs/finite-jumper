import pygame

class Tile:
    last_id = 0  # Class variable to keep track of the last assigned ID

    def __init__(self, screen, x, y, x_velocity, max_displacement=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.max_displacement = max_displacement
        self.displacement = 0
        self.x_velocity = x_velocity
        self.width = 100
        self.height = 10
        self.color = (255, 255, 255)
        self.id = Tile.last_id  # Assign a unique ID
        Tile.last_id += 1  # Increment the last assigned ID
        # self.text_surface = self.pre_render_text()

    def pre_render_text(self):
        font = pygame.font.Font(None, 28)
        text_surface = font.render(str(self.id), True, (255, 255, 255))
        return text_surface

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), border_radius=10)
        # self.screen.blit(self.text_surface, (self.x-20, self.y-20))

    def __str__(self):
        return f"tile {self.id} at ({self.x}, {self.y})"