import pygame
from classes import Bad_block
import globals


def easy_level():
    globals.blocks_count = 21
    this_is_a_victory = 300
    return globals.blocks_count, this_is_a_victory, "Super easy"


def first_level(bad_blocks):
    globals.blocks_count = 21
    this_is_a_victory = 300
    bad_blocks += [Bad_block(1, 1), Bad_block(1, 2), Bad_block(1, 3),
                   Bad_block(2, 1), Bad_block(2, 2), Bad_block(2, 3),
                   Bad_block(3, 1), Bad_block(3, 2), Bad_block(3, 3),
                   Bad_block(17, 1), Bad_block(17, 2), Bad_block(17, 3),
                   Bad_block(18, 1), Bad_block(18, 2), Bad_block(18, 3),
                   Bad_block(19, 1), Bad_block(19, 2), Bad_block(19, 3),
                   Bad_block(1, 17), Bad_block(2, 17), Bad_block(3, 17),
                   Bad_block(1, 18), Bad_block(2, 18), Bad_block(3, 18),
                   Bad_block(1, 19), Bad_block(2, 19), Bad_block(3, 19),
                   Bad_block(17, 17), Bad_block(17, 18), Bad_block(17, 19),
                   Bad_block(18, 17), Bad_block(18, 18), Bad_block(18, 19),
                   Bad_block(19, 17), Bad_block(19, 18), Bad_block(19, 19)]
    for i in range(globals.blocks_count):
        for j in range(globals.blocks_count):
            if (i == 10 and 3 < j < 17) or (j == 10 and 3 < i < 17):
                bad_blocks.append(Bad_block(i, j))
    return globals.blocks_count, this_is_a_victory, bad_blocks, "Easy"


def second_level(bad_blocks):
    font = pygame.font.SysFont('times New Roman', 30)
    this_is_a_victory = 180
    globals.blocks_count = 15
    for i_1 in range(globals.blocks_count):
        for j_1 in range(globals.blocks_count):
            if (j_1 == 1 and 2 < i_1 < 12) or \
                    (j_1 == 13 and 2 < i_1 < 12) or\
                    (j_1 == 7 and 2 < i_1 < 12):
                bad_blocks.append(Bad_block(i_1, j_1))
    return font, this_is_a_victory, globals.blocks_count, bad_blocks, "Medium"


def third_level(bad_blocks):
    font = pygame.font.SysFont('times New Roman', 20)
    this_is_a_victory = 60
    globals.blocks_count = 9
    for i_1 in range(globals.blocks_count):
        for j_1 in range(globals.blocks_count):
            if (j_1 == 1 and 1 < i_1 < 7) or (j_1 == 7 and 1 < i_1 < 7):
                bad_blocks.append(Bad_block(i_1, j_1))
    return font, this_is_a_victory, globals.blocks_count, bad_blocks, "Hard"
