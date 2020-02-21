import random
from Ladybug import *

class Engine:

    def __init__(self, width, height,screen):
        screen.fill( (255, 255, 255) )
        ladybugs = []
        numbers_of_ladybug = 100

        for i in range(1, numbers_of_ladybug ):
            randomX = random.randint( 0, width - 1 )
            randomY = random.randint( 0, height - 1 )
            ladybugs.append( Ladybug( randomX, randomY ) )

        for ladybug in ladybugs:
            ladybug.draw( screen )

    def update(self):
        is_over = False



