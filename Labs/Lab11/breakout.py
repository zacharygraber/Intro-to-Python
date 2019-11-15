import pygame
import sys
import random

pygame.init()

size = [500,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout!")

class Bar:
    def __init__(self, loc):
        self.loc = loc
    
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), self.loc)

    def move(self, direc):
        self.loc[0] += (6 * direc)

class Brick:
    def __init__(self, color, loc):
        self.color = color
        self.loc = loc
        self.destroy = False
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.loc)

    def destroyBrick(self):
        self.destroy = True

class Ball:
    def __init__(self, loc):
        self.loc = loc
    
    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), self.loc)
    
    def move(self, xoffset, yoffset):
        self.loc[0] += xoffset
        self.loc[1] += yoffset

cursor = Bar([212.5,400,75,3])
bricks = {i:Brick([random.randint(0,255) for i in range(3)], [i*50,0,48,48]) for i in range(0,10)}
ball = Ball([250,250,5,5])

if __name__ == "__main__":
    started = False
    while True:
        pygame.time.wait(33)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        inputs = pygame.key.get_pressed()
        if inputs[pygame.K_LEFT] and cursor.loc[0] > 0:
            cursor.move(-1)
        if inputs[pygame.K_RIGHT] and cursor.loc[0] < 425:
            cursor.move(1)
        
        if not started:
            ball.move(0,3)

        if ball.loc[1] == 400 and abs(ball.loc[0] - cursor.loc[0]) <= 

        screen.fill((0,0,0))
        cursor.draw(screen)
        ball.draw(screen)
        for i in bricks:
            if not bricks[i].destroy:
                bricks[i].draw(screen)

        pygame.display.flip()
        