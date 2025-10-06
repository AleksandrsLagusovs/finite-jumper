
import pygame

class Flag:
   
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 25
        self.height = 40
        self.image = pygame.image.load("assets/flag.png")
        self.captured = False

    def draw(self):
      
        if not self.captured:
            self.screen.blit(self.image, (self.x, self.y))