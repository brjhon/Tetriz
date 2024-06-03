import pygame
import random

# Configurações do jogo
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 10

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Formas dos blocos
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3],
     [3, 3]],

    [[4, 0],
     [4, 0],
     [4, 4]],

    [[0, 5],
     [0, 5],
     [5, 5]],

    [[0, 6],
     [6, 6],
     [6, 0]],

    [[7, 7],
     [7, 7]]
]


