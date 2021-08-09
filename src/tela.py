import pygame

try:
    pygame.init()
except:
    print("Erro. Programa não inicializado")


largura = 640
altura = 480

pygame.display.set_mode((largura, altura))
pygame.display.set_caption ("Mazegen")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    pygame.display.update()

pygame.quit()