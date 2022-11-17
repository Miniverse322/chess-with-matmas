import sys
import pygame


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Chess")

    try:
        image = pygame.image.load("chess_pieces.bmp").convert()
    except pygame.error as e:
        print("Unable to load image.")
        raise SystemExit(e)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        rect = pygame.Rect((68, 70, 85, 85))

        screen.fill((225, 225, 225))
        screen.blit(image, (0, 0), rect)
        pygame.display.flip()
        clock.tick(60)
