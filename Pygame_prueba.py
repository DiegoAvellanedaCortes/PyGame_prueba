from menu import menu
from controles import controles_Mov
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            controles_Mov(event)



    imgInicio=pygame.image.load("./img/Inicio.png").convert()
    screen.blit(imgInicio, [0,0])

    pygame.display.set_caption("Juego Mario") #Nombre de la ventana

    pygame.font.init()
    menu(screen)

    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()