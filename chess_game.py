import sys
import pygame

PIECE_SIZE = 100

def draw_piece(x, y, rect):
    screen.blit(image, (PIECE_SIZE * x, PIECE_SIZE * y), rect)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((PIECE_SIZE*8, PIECE_SIZE*8))
    pygame.display.set_caption("Chess")

    try:
        image = pygame.image.load("chess_pieces.png").convert_alpha()
    except pygame.error as e:
        print("Unable to load image.")
        raise SystemExit(e)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((225, 225, 225))

        empty = pygame.Rect((0, 0, 0, 0))
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

        pieces = [
            rect_rook_black,
            rect_knight_black,
            rect_bishop_black,
            rect_queen_black,
            rect_king_black,
            rect_bishop_black,
            rect_knight_black,
            rect_rook_black,

            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,
            rect_pawn_black,

            empty, empty, empty, empty, empty, empty, empty, empty,
            empty, empty, empty, empty, empty, empty, empty, empty,
            empty, empty, empty, empty, empty, empty, empty, empty,
            empty, empty, empty, empty, empty, empty, empty, empty,


            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,
            rect_pawn_white,

            rect_rook_white,
            rect_knight_white,
            rect_bishop_white,
            rect_queen_white,
            rect_king_white,
            rect_bishop_white,
            rect_knight_white,
            rect_rook_white,
        ]
        print(pygame.mouse.get_pressed())
        print(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 35, 38), pygame.Rect(100, 100, 100, 100))

        # for x in range(8):
        #     for y in range(8):
        #         draw_piece(x, y, pieces[y * 8 + x])

        for i in range(64):
            draw_piece(i % 8, i // 8, pieces[i])

        pygame.display.flip()
        clock.tick(60)
