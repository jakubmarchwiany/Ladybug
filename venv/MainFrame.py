# Glowne Okno Aplikacji

import pygame,sys,os

pygame.init()
pygame.display.set_caption( "Biedronkowa Zawierucha" )

height = 500
widght = 500

screen = pygame.display.set_mode((height, weight))




show = 0

while True:
    if show==0:
        pygame.display.update()
        grafika=pygame.image.load(os.path.join("MenuPic.png"))
        screen.blit( grafika, (0, 0) )



