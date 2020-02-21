# Klasa Biedronka

import os
import pygame


class Ladybug:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.graphic = pygame.image.load(os.path.join("biedrona.png"))

    def print_position(self):
        print("x = " + str(self.x) + ", y = " + str(self.y))

    def draw(self, surface):
        surface.blit(self.graphic, int(self.x), int(self.y))

    def move(self, x, y):
        self.x = x
        self.y = y
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
