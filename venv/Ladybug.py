# Klasa Biedronka

import pygame


class Ladybug:
    radius = 5
    color = (255, 0, 0)

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_position(self):
        print("x = " + str(self.x) + ", y = " + str(self.y))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, x, y):
        self.x = x
        self.y = y
