from levels import easy_level, first_level, second_level, third_level


def pause_menu(level, bad_blocks, font):
    while True:
        if level == 1:
            blocks_count, this_is_a_victory,\
                bad_blocks, name = first_level(bad_blocks)
            return blocks_count, this_is_a_victory,\
                bad_blocks, name, font
        elif level == 2:
            font, this_is_a_victory, blocks_count,\
                bad_blocks, name = second_level(bad_blocks)
            return blocks_count, this_is_a_victory,\
                bad_blocks, name, font
        elif level == 4:
            blocks_count, this_is_a_victory, name = easy_level()
            return blocks_count, this_is_a_victory,\
                bad_blocks, name, font
        elif level == 3:
            font, this_is_a_victory, blocks_count,\
                bad_blocks, name = third_level(bad_blocks)
            return blocks_count, this_is_a_victory,\
                bad_blocks, name, font
        elif level == -1:
            continue
