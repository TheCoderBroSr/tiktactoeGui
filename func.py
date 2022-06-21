import sys
import pygame

pygame.font.init()
MARKER = pygame.font.SysFont('Comic Sans Ms', 150)

def end():
    pygame.quit()
    sys.exit()

def init_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def gridCoordinates(pos, surf):
    x, y = pos
    gap = surf.get_height()//3

    return (y//gap, x//gap) #Flipped due to pygame's coordinate system

def draw_bars(bars, color, surf):
    for bar in bars:
        pygame.draw.rect(surf, color, bar)

def display_board(board, color, surf):
    #color is a list, where in first index is the colors of the markers,
    #and in second is the color of the bars
    height, width = surf.get_height(), surf.get_width() #Getting height and width of surface

    gap = height//3 #Getting the gap in the grid

    horizontal_bars = [pygame.Rect(i*gap, 0, 10, height) for i in range(1, 3)] #Getting horizontal bars of the grid
    vertical_bars = [pygame.Rect(0, i*gap, width, 10) for i in range(1, 3)] #Getting vertical bars of the grid

    #Drawing individual bar of each type
    draw_bars(horizontal_bars, color[1], surf)
    draw_bars(vertical_bars, color[1], surf)

    #Drawing value of each grid cell
    for i in range(len(board[0])):
        for j in range(len(board[i])):
            val = board[i][j]
            color_index = 0

            if val==" ":
                continue
            
            if val == "O":
                color_index = 1
            
            val = MARKER.render(val, 1, color[0][color_index])
            surf.blit(val, (gap*j - (val.get_width()//2) + (gap//2), gap*i - (val.get_height()//2) + (gap//2)))