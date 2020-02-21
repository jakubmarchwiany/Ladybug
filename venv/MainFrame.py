# Glowne Okno Aplikacji

import pygame
import random
from Ladybug import *

pygame.init()
pygame.display.set_caption("Biedronkowa Zawierucha")

height = 500
width = 500

screen = pygame.display.set_mode((height, width))
white = (255, 255, 255)
screen.fill(white)

ladybugs = []

numbers_of_ladybug = 100

for i in range(1, numbers_of_ladybug):
    randomX = random.randint(0, width - 1)
    randomY = random.randint(0, height - 1)

    ladybugs.append(Ladybug(randomX, randomY))

for ladybug in ladybugs:
    ladybug.draw(screen)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

