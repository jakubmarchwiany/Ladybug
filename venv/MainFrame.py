# Glowne Okno Aplikacji

import pygame,sys,os

pygame.init()
pygame.display.set_caption( "Biedronkowa Zawierucha" )

height = 500
widght = 500

screen = pygame.display.set_mode((height, widght))




show = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                show=1


    if show==0:
        grafika=pygame.image.load(os.path.join("MenuPic.png"))
        screen.blit( grafika, (0, 0) )
    if show==1:
        screen.fill((0,0,0))



    pygame.display.update()