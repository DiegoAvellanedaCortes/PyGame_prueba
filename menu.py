import pygame

def menu (screen):
    fuente = pygame.font.Font(None, 100)

    inicio=pygame.Rect(800, 350, 460,80)
    salir=pygame.Rect(900, 450, 200,80)

    pygame.draw.rect(screen, (255, 255, 255), inicio, 0 )
    pygame.draw.rect(screen, (255, 255, 255), salir, 0 )

    text = "Iniciar Juego"
    menu_uno = fuente.render(text, True, (0,0,0))
    screen.blit(menu_uno, (inicio.x+(inicio.width-menu_uno.get_width())/2 , inicio.y+(inicio.height-menu_uno.get_height())/2))
    
    text = "Salir"
    menu_dos = fuente.render(text, True, (0,0,0))
    screen.blit(menu_dos, (salir.x+(salir.width-menu_dos.get_width())/2 , salir.y+(salir.height-menu_dos.get_height())/2))
