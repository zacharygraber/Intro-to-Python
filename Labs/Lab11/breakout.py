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
# bricks = {i:Brick([random.randint(0,255) for i in range(3)], [i*(size[0]/10),30,49,49]) for i in range(0,10)}
bricks = {}
for i in range(10):
    bricks[i] = Brick((random.randint(50,255),0,0), [i*(size[0]/10),30,49,29])
for i in range(10,16):
    bricks[i] = Brick((255,random.randint(80,180),0), [(i-10)*(size[0]/6),60,82,39])
for i in range(16,28):
    bricks[i] = Brick((255,255,random.randint(0,120)), [(i-16)*(42),100,41,34])
for i in range(28,38):
    bricks[i] = Brick((0,random.randint(50,255),0), [(i-28)*(size[0]/10),135,49,49])

# testBrick = Brick((255,255,255),[50,50,50,50])
# bricks = {0:testBrick}
ball = Ball([250,250,5,5])

if __name__ == "__main__":
    def gameLoop():
        started = False
        while True:
            pygame.time.wait(16)

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
                yd = 3
                xd = 0

            if ball.loc[1] >= 397 and ball.loc[1] <= 403 and (ball.loc[0] >= cursor.loc[0] and ball.loc[0] <= (cursor.loc[0] + 75)):
                started = True
                yd = -3
                xd = (37.5 - (ball.loc[0] - cursor.loc[0])) * -0.1
            
            if ball.loc[0] < 0 or ball.loc[0] > size[1]:
                xd *= -1
            
            if ball.loc[1] < 0:
                yd *= -1

            for i in bricks:
                if not bricks[i].destroy:
                    #bottom
                    if ball.loc[1] <= (bricks[i].loc[1] + bricks[i].loc[3]) and ball.loc[1] >= (bricks[i].loc[1] + (bricks[i].loc[3] - 3)):
                        if ball.loc[0] >= bricks[i].loc[0] and ball.loc[0] <= (bricks[i].loc[0] + bricks[i].loc[2]):
                            yd *= -1
                            bricks[i].destroyBrick()
                    #top
                    elif ball.loc[1] >= bricks[i].loc[1] and ball.loc[1] <= (bricks[i].loc[3] + 4):
                        if ball.loc[0] >= bricks[i].loc[0] and ball.loc[0] <= (bricks[i].loc[0] + bricks[i].loc[2]):
                            yd *= -1
                            bricks[i].destroyBrick()
                    #left
                    elif ball.loc[0] >= bricks[i].loc[0] and ball.loc[0] <= (bricks[i].loc[0] + 10):
                        if ball.loc[1] >= bricks[i].loc[1] and ball.loc[1] <= (bricks[i].loc[1] + bricks[i].loc[3]):
                            xd *= -1
                            bricks[i].destroyBrick()
                    #right
                    elif ball.loc[0] <= (bricks[i].loc[0] + bricks[i].loc[2]) and ball.loc[0] >= (bricks[i].loc[0] + (bricks[i].loc[2] - 10)):
                        if ball.loc[1] >= bricks[i].loc[1] and ball.loc[1] <= (bricks[i].loc[1] + bricks[i].loc[3]):
                            xd *= -1
                            bricks[i].destroyBrick()


            ball.move(xd,yd)

            screen.fill((0,0,0))
            cursor.draw(screen)
            ball.draw(screen)
            for i in bricks:
                if not bricks[i].destroy:
                    bricks[i].draw(screen)

            pygame.display.flip()
    while True:
        gameLoop()
        