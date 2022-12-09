import pygame

pygame.init()

SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((5, 255, 5))

    pygame.display.flip()

pygame.quit()