import pygame
import sys
pygame.init()
window = pygame.display.set_mode((500,700))
pygame.display.set_caption("Sky Flyers yuh yeet ahlie")
running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            pygame.draw.rect(window, (0,0,255), [400, 600, 100], 7)
        pygame.display.flip()
    pygame.display.update()
    window.fill((0,0,0))
sys.exit()