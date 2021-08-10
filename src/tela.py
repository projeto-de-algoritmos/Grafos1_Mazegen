import pygame

import networkx as nx

import random

import time

try:
    pygame.init()
except:
    print("Erro. Programa não inicializado")


WIDTH = 500
HEIGHT = 600
FPS = 30

tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Mazegen")


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)

w=20

# build the grid
def build_grid(x, y, w):
    x = 0
    y = 0 
    for i in range(1,21):
        x = 0                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(tela, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(tela, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(tela, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(tela, WHITE, [x, y + w], [x, y])           # left of cell
            x = x + 20                                                    # move cell to new position


def up(x, y):
    x=20*x
    y=20*y
    pygame.draw.rect(tela, GREEN, (x + 1, y - w + 1, 19, 39), 0)         # draw a rectangle twice the width of the cell
    pygame.display.update()                                              # to animate the wall being removed


def down(x, y):   
    x=20*x
    y=20*y
    pygame.draw.rect(tela, GREEN, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def left(x, y):
    x=20*x
    y=20*y
    pygame.draw.rect(tela, GREEN, (x - 20 +1, y +1, 39, 19), 0)
    pygame.display.update()


def right(x, y):
    x=20*x
    y=20*y
    pygame.draw.rect(tela, GREEN, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


#Random DFS

G = nx.grid_2d_graph(19,19)


def randUnvisitedNeighbor(vertex):
    unvNeigh = []
    neigh = G[vertex]
    for (x, y) in neigh:
        if G.nodes[(x, y)] != {'visited': 1} :
            unvNeigh.append((x, y))

    if len(unvNeigh) >= 1:
        chosenVertex = random.choice(unvNeigh)

    else:
        chosenVertex = False

    return chosenVertex

def moveCell(vertex, nextVertex):
    (x, y) = vertex
    (x2, y2) = nextVertex

    if x == x2:
        if y < y2:
            time.sleep(.05)
            right(x2, y2)
        else:
            time.sleep(.05)
            left(x2, y2)
    else:
        if x < x2:
            time.sleep(.05)
            down(x2, y2)
        else:
            time.sleep(.05)
            up(x2, y2)

#Instead of iterating through the neigbors it chooses one randomly
def randomDFS(vertex):
    G.nodes[vertex]['visited'] = 1
    nextVertex = randUnvisitedNeighbor(vertex)

    while nextVertex:
        moveCell(vertex, nextVertex)
        randomDFS(nextVertex)
        nextVertex = randUnvisitedNeighbor(vertex)



def createMaze():
    startVertex = (0, 0)
    randomDFS(startVertex)

build_grid(40, 0, 20) 
createMaze()

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    pygame.display.update()

pygame.quit()