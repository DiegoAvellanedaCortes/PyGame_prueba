from menu import menu
from controles import controles_Mov
from juego import juego
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
inicio=pygame.Rect(800, 350, 460,80)
salir=pygame.Rect(900, 450, 200,80)

imgInicio=pygame.image.load("./img/Inicio.png").convert()
fondoJuego=pygame.image.load("./img/Fondo.png").convert()
menuFondo=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            controles_Mov(event)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if inicio.collidepoint(pygame.mouse.get_pos()):
                menuFondo=False
                screen.blit(fondoJuego, [0,0])

            elif salir.collidepoint(pygame.mouse.get_pos()):
                running=False

    if menuFondo==True:
        screen.blit(imgInicio, [0,0])
        menu(inicio, salir, screen)

    

    pygame.display.set_caption("Juego Mario") #Nombre de la ventana

    pygame.font.init()


    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()

