import pygame
from Blocks import BadBlock
import config


def easy_level():
    config.blocks_count = 21
    this_is_a_victory = 300
    return config.blocks_count, this_is_a_victory, "Super easy"


def first_level(bad_blocks):
    config.blocks_count = 21
    this_is_a_victory = 300
    bad_blocks += [
        BadBlock(1, 1), BadBlock(1, 2), BadBlock(1, 3),
        BadBlock(2, 1), BadBlock(2, 2), BadBlock(2, 3),
        BadBlock(3, 1), BadBlock(3, 2), BadBlock(3, 3),
        BadBlock(17, 1), BadBlock(17, 2), BadBlock(17, 3),
        BadBlock(18, 1), BadBlock(18, 2), BadBlock(18, 3),
        BadBlock(19, 1), BadBlock(19, 2), BadBlock(19, 3),
        BadBlock(1, 17), BadBlock(2, 17), BadBlock(3, 17),
        BadBlock(1, 18), BadBlock(2, 18), BadBlock(3, 18),
        BadBlock(1, 19), BadBlock(2, 19), BadBlock(3, 19),
        BadBlock(17, 17), BadBlock(17, 18), BadBlock(17, 19),
        BadBlock(18, 17), BadBlock(18, 18), BadBlock(18, 19),
        BadBlock(19, 17), BadBlock(19, 18), BadBlock(19, 19)
    ]
    for i in range(config.blocks_count):
        for j in range(config.blocks_count):
            if (i == 10 and 3 < j < 17) or (j == 10 and 3 < i < 17):
                bad_blocks.append(BadBlock(i, j))
    return config.blocks_count, this_is_a_victory, bad_blocks, "Easy"


def second_level(bad_blocks):
    font = pygame.font.SysFont('times New Roman', 30)
    this_is_a_victory = 180
    config.blocks_count = 15
    for i_1 in range(config.blocks_count):
        for j_1 in range(config.blocks_count):
            if (j_1 == 1 and 2 < i_1 < 12) or \
                    (j_1 == 13 and 2 < i_1 < 12) or \
                    (j_1 == 7 and 2 < i_1 < 12):
                bad_blocks.append(BadBlock(i_1, j_1))
    return font, this_is_a_victory, config.blocks_count, bad_blocks, "Medium"


def third_level(bad_blocks):
    font = pygame.font.SysFont('times New Roman', 20)
    this_is_a_victory = 60
    config.blocks_count = 9
    for i_1 in range(config.blocks_count):
        for j_1 in range(config.blocks_count):
            if (j_1 == 1 and 1 < i_1 < 7) or (j_1 == 7 and 1 < i_1 < 7):
                bad_blocks.append(BadBlock(i_1, j_1))
    return font, this_is_a_victory, config.blocks_count, bad_blocks, "Hard"
