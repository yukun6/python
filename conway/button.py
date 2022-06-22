import pygame


class Button():
    def __init__(self, screen, x, y, a, b, width, color, bitcolor, font, size, text):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.width = width
        self.color = color
        self.bitcolor = bitcolor
        self.text = text
        self.font = pygame.font.Font(font, size)
        self.flag = False

    def draw_text(self):
        label = self.font.render(self.text, self.width, self.color)
        self.screen.blit(label, (self.x + 2, self.y + 10))

    def draw_button(self):
        if not self.flag:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.a, self.b), self.width)
        else:
            pygame.draw.rect(self.screen, self.bitcolor, (self.x, self.y, self.a, self.b), self.width)

    def check_click(self, position):
        x_match = self.x < position[0] < self.x + self.a
        y_match = self.y < position[1] < self.y + self.b

        if x_match and y_match:
            self.flag = True
        else:
            self.flag = False
        return self.flag
