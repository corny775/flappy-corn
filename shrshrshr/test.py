import pygame


pygame.init()


surface = pygame.display.set_mode((700, 700))
color = (255, 0, 0)
rectangle = pygame.Rect(0,0,700,700)


while True:
    pygame.draw.rect(surface, color, rectangle)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)