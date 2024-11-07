import pygame


def controles_Mov(event):
    if event.key==pygame.K_DOWN:
        print("Abajo")
    elif event.key==pygame.K_UP:
        print("Arriba")
    elif event.key==pygame.K_LEFT:
        print("Izquierda")
    elif event.key==pygame.K_RIGHT:
        print("Derecha")