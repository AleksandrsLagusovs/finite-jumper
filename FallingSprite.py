import pygame

class FallingSprite:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = 0
        self.image = pygame.image.load("assets/down.png")

    def rotate(self):
        self.angle += 10
        if self.angle >= 360:
            self.angle = 0
        self.image = pygame.transform.rotate(pygame.image.load("assets/down.png"), self.angle)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.rotate()
        if self.y >= 720:
            return True # Indicate that this object should be deleted
        return False

    def delete(self):
        self.image = None
        self.x = None
        self.y = None
        self.angle = None
        self.screen = None