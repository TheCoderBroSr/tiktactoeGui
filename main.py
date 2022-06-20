import pygame
from func import *

pygame.init()
board = init_board()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("TicTacToe GUI"))

BLACK = (5, 0, 20)
BLUE = (10, 23, 123)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end()

    WIN.fill(BLACK)
    display_board(board, BLUE, WIN)

    pygame.display.update()
        
