import pygame, sys

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,600), 0, 32)
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))
    screen.blit(background, (0,0))
    pygame.display.flip()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_f:
                    screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)

