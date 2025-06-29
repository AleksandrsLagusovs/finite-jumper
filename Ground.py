import pygame

class Ground():
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 720-20
        self.width = 1280
        self.height = 20
        self.color = (255, 255, 255)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))