import pygame
from Game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Finite Jumper")
    game = Game(screen)
    game.generate_tiles(screen)
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if not game.victory:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game.jumper.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        game.jumper.moving_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        game.jumper.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        game.jumper.moving_right = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()