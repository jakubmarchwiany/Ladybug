# Glowne Okno Aplikacji

import pygame, sys, os, random
from Ladybug import *
from Engine import *

pygame.init()
pygame.display.set_caption( "Biedronkowa Zawierucha" )

height = 500
width = 500

screen = pygame.display.set_mode( (height, width) )

show = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show = 1
                engine = Engine( width, height, screen )

    if show == 0:
        background = pygame.image.load(os.path.join("MenuPic.png"))
        screen.blit(background, (0, 0))
    if show == 1:
       if(engine.end)
            print("Koniec gry")

    pygame.display.update()
