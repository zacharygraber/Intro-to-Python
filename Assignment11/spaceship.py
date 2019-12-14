import math
import pygame
import sys

#INPUT c, a complex number tuple, and i, a max number of iterations
#RETURN Number of iterations needed to leave the circle of radius two; returns -1 if max is reached
def mandelbrot(c,maxIter):
    z = (0,0)
    i = 0
    while i < maxIter:
        mod = math.sqrt(z[0]**2 + z[1]**2)
        if mod >= 2:
            return i
        else:
            z = (((z[0]*z[0])-(z[1]*z[1])) + c[0], ((z[0]*z[1]) + (z[1]*z[0])) + c[1])
            i += 1
    return -1
pygame.init()

size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mandelbrot")
screen.fill((255,255,255))

pixelArray = pygame.PixelArray(screen)

for x in range(size[0]):
    for y in range(size[1]):
        m = mandelbrot((-2 + (x / 300),-1 + (y / 300)),60)
        if m == -1:
            pixelArray[x,y] = (0,0,0)
        else:
            pixelArray[x,y] = (m * 4,m * 4,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
