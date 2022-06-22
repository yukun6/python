import pygame.draw


class Block():
    def __init__(self, screen, x, y, a):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = a
        self.color = (255, 255, 255)

    def draw(self):
        position = (self.x, self.y, self.a, self.a)
        pygame.draw.rect(self.screen, self.color, position)
