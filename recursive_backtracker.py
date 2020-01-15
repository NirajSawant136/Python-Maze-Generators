'''
This is a maze generator made in python using pygame module
I used the Recursive Backtrack algorithm to make this
A cool project!
'''

import random
import pygame
import time

WIDTH = 685
HEIGHT = 685
fps = 30

WHITE = (255,255,255)
RED = (255 , 38 , 38)

pygame.init()
pygame.mixer.init()
MAZE = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock()

def buildMaze(maze , size):
        x = 1
        y = 1
        count = 1
        soln = [(x,y-1),(x,y)]
        stack = [(x,y)]
        randTile( maze , stack , soln , size )

def stopCarving(maze , size):
        count = 0
        for i in range(1,size,2):
                for j in range(1,size,2):
                        if maze[i][j] == 1:
                                count += 1

        return count != ((size-1)//2)**2
                                       
def randTile(maze , stack , soln , size):
        if stopCarving(maze , size) and len(stack) != 0:
                
                x , y = stack[len(stack)-1]
                maze[x][y] = 1
                time.sleep(0.1)
                pygame.draw.rect(MAZE , WHITE , (x*15,y*15,15,15),0)
                pygame.display.update()
                randList = []
                if x + 2 < size-1:
                        if maze[x+2][y] == 0:
                                randList.append(1)
                if x - 2 > 0:
                        if maze[x-2][y] == 0:
                                randList.append(2)
                if y + 2 < size-1:
                        if maze[x][y+2] == 0:
                                randList.append(3)
                if y - 2 > 0:
                        if maze[x][y - 2] == 0:
                                randList.append(4)
                
                if len(randList) == 0:
                        stack.pop()
                        if (size-2,size-2) not in soln:
                                soln.pop()
                                soln.pop()
                        randTile(maze , stack ,soln ,  size)
                        
                else:
                        options = random.choice(randList)
                        if options == 1:
                                x = x + 2
                                stack.append((x,y))
                                if (size-2,size-2) not in soln:
                                        soln.append((x-1,y))
                                        soln.append((x,y))
                                maze[x-1][y] = 1
                                pygame.draw.rect(MAZE , WHITE , ((x-1)*15,y*15,15,15),0)
                                pygame.display.update()
                                randTile(maze , stack , soln , size)
                        elif options == 2:
                                x = x - 2
                                stack.append((x,y))
                                if (size-2,size-2) not in soln:
                                        soln.append((x+1,y))
                                        soln.append((x,y))
                                maze[x+1][y] = 1
                                pygame.draw.rect(MAZE , WHITE , ((x+1)*15,y*15,15,15),0)
                                pygame.display.update()
                                randTile(maze , stack , soln , size)
                        elif options == 3:
                                y = y + 2
                                stack.append((x,y))
                                if (size-2,size-2) not in soln:
                                        soln.append((x,y-1))
                                        soln.append((x,y))
                                maze[x][y-1] = 1
                                pygame.draw.rect(MAZE , WHITE , (x*15,(y-1)*15,15,15),0)
                                pygame.display.update()
                                randTile(maze , stack , soln , size)
                        elif options == 4:
                                y = y - 2
                                stack.append((x,y))
                                if (size-2,size-2) not in soln:
                                        soln.append((x,y+1))
                                        soln.append((x,y))
                                maze[x][y+1] = 1
                                pygame.draw.rect(MAZE , WHITE , (x*15,(y+1)*15,15,15),0)
                                pygame.display.update()
                                randTile(maze , stack , soln , size)


n = 45
maze = [[0 for i in range(n)]for j in range(n)]
buildMaze(maze , n)

run = True
while run:
        clock.tick(fps)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        run = False
