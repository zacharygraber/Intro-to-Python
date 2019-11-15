import pygame
import sys
import random as rn

pygame.init()
 
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)
DARK_GREEN = (0,100,0)

class Rectangle:
    """
    Refer to the instructions if you need to modify this.
    """

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
  
       
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("C200 CHANGE")


r = Rectangle(RED, [0, 0, 20, 20])
r2 = Rectangle(RED, [281,0,20,20])

if __name__ == "__main__":
    while True:
        
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
        screen.fill(WHITE)
    
        r.my_draw(screen)
        r2.my_draw(screen)
        
        if r.loc[0] > 280:
            xd = -rn.randint(1,3)
            r.color = DARK_GREEN
        if r.loc[1] > 280:
            yd = -rn.randint(1,3)
            r.color = BLUE
        if r.loc[0] < 10:
            xd = rn.randint(1,3)
            r.color = RED
        if r.loc[1] < 10:
            yd = rn.randint(1,3)
            r.color = YELLOW
        r.my_move(xd,yd)

        if r2.loc[0] > 280:
            xd2 = -rn.randint(1,3)
            r2.color = DARK_GREEN
        if r2.loc[1] > 280:
            yd2 = -rn.randint(1,3)
            r2.color = BLUE
        if r2.loc[0] < 10:
            xd2 = rn.randint(1,3)
            r2.color = RED
        if r2.loc[1] < 10:
            yd2 = rn.randint(1,3)
            r2.color = YELLOW
        r2.my_move(xd2,yd2)

        if abs(r.loc[0] - r2.loc[0]) < ((r.loc[2] / 2) + (r2.loc[2] / 2)) and abs(r.loc[1] - r2.loc[1]) < ((r.loc[3] / 2)+(r2.loc[3] / 2)):
            xd *= -1
            yd *= -1
            xd2 *= -1
            yd2 *= -1
        r.my_move(xd,yd)
        r2.my_move(xd2,yd2)

        pygame.display.flip()