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

class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def draw(self, surface):
        for y, row in enumerate(self.shape[self.rotation]):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(surface, self.color, (self.x * BLOCK_SIZE + x * BLOCK_SIZE, self.y * BLOCK_SIZE + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def create_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def check_collision(grid, block):
    for y, row in enumerate(block.shape[block.rotation]):
        for x, val in enumerate(row):
            if val and (block.y + y >= GRID_HEIGHT or block.x + x < 0 or block.x + x >= GRID_WIDTH or grid[block.y + y][block.x + x]):
                return True
    return False

def merge_grid(grid, block):
    for y, row in enumerate(block.shape[block.rotation]):
        for x, val in enumerate(row):
            if val:
                grid[block.y + y][block.x + x] = block.color

def clear_rows(grid):
    full_rows = [row for row in range(GRID_HEIGHT) if all(grid[row])]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0 for _ in range(GRID_WIDTH)])

def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val:
                pygame.draw.rect(surface, val, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_game_over(surface):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Game Over!", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    grid = create_grid()
    current_block = Block(random.choice(SHAPES), random.choice([RED, BLUE, GREEN, YELLOW]))

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_LEFT:
                    current_block.move_left()
                    if check_collision(grid, current_block):
                        current_block.move_right()
                elif event.key == pygame.K_RIGHT:
                    current_block.move_right()
                    if check_collision(grid, current_block):
                        current_block.move_left()
                elif event.key == pygame.K_DOWN:
                    current_block.move_down()
                    if check_collision(grid, current_block):
                        current_block.move_up()
                elif event.key == pygame.K_SPACE:
                    current_block.rotate()
                    if check_collision(grid, current_block):
                        current_block.rotate_back()
        
        if not game_over:
            current_block.move_down()
            if check_collision(grid, current_block):
                current_block.move_up()
                merge_grid(grid, current_block)
                clear_rows(grid)
                current_block = Block(random.choice(SHAPES), random.choice([RED, BLUE, GREEN, YELLOW]))
                if check_collision(grid, current_block):
                    game_over = True

        screen.fill(BLACK)
        draw_grid(screen, grid)
        current_block.draw(screen)

        if game_over:
            draw_game_over(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
