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

        rect_rook_black = pygame.Rect((PIECE_SIZE * 2, 0, PIECE_SIZE, PIECE_SIZE))
        rect_knight_black = pygame.Rect((PIECE_SIZE * 4, 0, PIECE_SIZE, PIECE_SIZE))
        rect_king_black = pygame.Rect((0, 0, PIECE_SIZE, PIECE_SIZE))
        rect_queen_black = pygame.Rect((PIECE_SIZE, 0, PIECE_SIZE, PIECE_SIZE))
        rect_bishop_black = pygame.Rect((PIECE_SIZE * 3, 0, PIECE_SIZE, PIECE_SIZE))
        rect_pawn_black = pygame.Rect((PIECE_SIZE * 5, 0, PIECE_SIZE, PIECE_SIZE))

        rect_rook_white = pygame.Rect((PIECE_SIZE * 2, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        rect_knight_white = pygame.Rect((PIECE_SIZE * 4, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        rect_king_white = pygame.Rect((0, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        rect_queen_white = pygame.Rect((PIECE_SIZE, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        rect_bishop_white = pygame.Rect((PIECE_SIZE * 3, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))
        rect_pawn_white = pygame.Rect((PIECE_SIZE * 5, PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))

        screen.blit(image, (PIECE_SIZE * 0, 0), rect_rook_black)
        screen.blit(image, (PIECE_SIZE * 1, 0), rect_knight_black)
        screen.blit(image, (PIECE_SIZE * 2, 0), rect_bishop_black)
        screen.blit(image, (PIECE_SIZE * 3, 0), rect_queen_black)
        screen.blit(image, (PIECE_SIZE * 4, 0), rect_king_black)
        screen.blit(image, (PIECE_SIZE * 5, 0), rect_bishop_black)
        screen.blit(image, (PIECE_SIZE * 6, 0), rect_knight_black)
        screen.blit(image, (PIECE_SIZE * 7, 0), rect_rook_black)
        
        for i in range(8):
            screen.blit(image, (PIECE_SIZE * i, PIECE_SIZE), rect_pawn_black)

        for i in range(8):
            screen.blit(image, (PIECE_SIZE * i, PIECE_SIZE*6), rect_pawn_white)

        screen.blit(image, (PIECE_SIZE * 0, PIECE_SIZE*7), rect_rook_white)
        screen.blit(image, (PIECE_SIZE * 1, PIECE_SIZE*7), rect_knight_white)
        screen.blit(image, (PIECE_SIZE * 2, PIECE_SIZE*7), rect_bishop_white)
        screen.blit(image, (PIECE_SIZE * 3, PIECE_SIZE*7), rect_queen_white)
        screen.blit(image, (PIECE_SIZE * 4, PIECE_SIZE*7), rect_king_white)
        screen.blit(image, (PIECE_SIZE * 5, PIECE_SIZE*7), rect_bishop_white)
        screen.blit(image, (PIECE_SIZE * 6, PIECE_SIZE*7), rect_knight_white)
        screen.blit(image, (PIECE_SIZE * 7, PIECE_SIZE*7), rect_rook_white)

        pygame.display.flip()
        clock.tick(60)
