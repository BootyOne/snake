import pygame
from Blocks import SnakeBlock

pygame.init()

pygame.display.set_caption("Змейка")
frame_color = 0, 0, 255
white = 255, 255, 255
blue = 175, 238, 238
red = 224, 0, 0
black = 0, 0, 0
header_color = 25, 25, 112
snake_color = 0, 102, 0
block_size = 30
margin = 1
header_margin = 70
timer = pygame.time.Clock()
can_move = True
total = 0
font = pygame.font.SysFont('times New Roman', 36)
speed = 1
lives = 3
d_row = 0
d_col = 1
this_is_a_victory = 0
snake_blocks = [SnakeBlock(0, 0), SnakeBlock(0, 1), SnakeBlock(0, 2)]
bad_blocks = []
blocks_count = 21
size = [30 * 21 + 2 * 30 + 1 * 21, 30 * 21 + 2 * 30 + 1 * 21 + 71]
screen = pygame.display.set_mode(size)
