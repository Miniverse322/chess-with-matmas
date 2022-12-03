import sys
import pygame

PIECE_SIZE = 100

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((PIECE_SIZE*8, PIECE_SIZE*8))
    pygame.display.set_caption("Chess")

    try:
        image = pygame.image.load("chess_pieces.png").convert()
    except pygame.error as e:
        print("Unable to load image.")
        raise SystemExit(e)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((225, 225, 225))

        rect_rook = pygame.Rect((PIECE_SIZE*2, 0, PIECE_SIZE, PIECE_SIZE))
        rect_knight = pygame.Rect((PIECE_SIZE*4, 0, PIECE_SIZE, PIECE_SIZE))
        rect_king = pygame.Rect((0, 0, PIECE_SIZE, PIECE_SIZE))
        rect_queen = pygame.Rect((PIECE_SIZE, 0, PIECE_SIZE, PIECE_SIZE))
        rect_bishop = pygame.Rect((PIECE_SIZE*3, 0, PIECE_SIZE, PIECE_SIZE))
        rect_pawn = pygame.Rect((PIECE_SIZE*5, 0, PIECE_SIZE, PIECE_SIZE))

        screen.blit(image, (PIECE_SIZE*0, 0), rect_rook)
        screen.blit(image, (PIECE_SIZE*1, 0), rect_knight)
        screen.blit(image, (PIECE_SIZE*2, 0), rect_bishop)
        screen.blit(image, (PIECE_SIZE*3, 0), rect_queen)
        screen.blit(image, (PIECE_SIZE*4, 0), rect_king)
        screen.blit(image, (PIECE_SIZE*5, 0), rect_bishop)
        screen.blit(image, (PIECE_SIZE*6, 0), rect_knight)
        screen.blit(image, (PIECE_SIZE*7, 0), rect_rook)
        
        screen.blit(image, (PIECE_SIZE*0, PIECE_SIZE), rect_pawn)
        screen.blit(image, (PIECE_SIZE*1, PIECE_SIZE), rect_pawn)
        screen.blit(image, (PIECE_SIZE*2, PIECE_SIZE), rect_pawn)
        screen.blit(image, (PIECE_SIZE*3, PIECE_SIZE), rect_pawn)

        pygame.display.flip()
        clock.tick(60)
