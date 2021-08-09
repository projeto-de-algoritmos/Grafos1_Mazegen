import pygame

import networkx as nx


try:
    pygame.init()
except:
    print("Erro. Programa não inicializado")


largura = 640
altura = 480

pygame.display.set_mode((largura, altura))
pygame.display.set_caption ("Mazegen")


#Random DFS

G = nx.grid_2d_graph(20,20)


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



sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    pygame.display.update()

pygame.quit()