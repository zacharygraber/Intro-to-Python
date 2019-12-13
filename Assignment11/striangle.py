import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    z = math.sqrt(width**2 - (width / 2)**2)

    top = (loc[0] + (width / 2), loc[1])
    left = (loc[0],loc[1] + z)
    right = (loc[0] + width,loc[1] + z)
    
    return (top,left,right)

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, [rn.randint(0,255) for i in range(3)], (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    draw_triangle(loc,width)
    if width > 5:
        z = math.sqrt(width**2 - (width / 2)**2)

        newLocTop = (loc[0] + (width/4),loc[1])
        newLocLeft = (loc[0],loc[1] + (z/2))
        newLocRight = (loc[0] + (width / 2),loc[1] + (z / 2))
        s(newLocTop,width / 2)
        s(newLocLeft, width / 2)
        s(newLocRight, width / 2)
    pass

s((0,0),440)

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()