from config import screen, block_size, margin, header_margin

import pygame


def draw_block(_color, _row, _column):
    pygame.draw.rect(
        screen, _color,
        [
            block_size + _column * block_size + margin * (_column + 1),
            header_margin + block_size + _row * block_size + margin * (_row + 1), block_size, block_size
        ]
    )