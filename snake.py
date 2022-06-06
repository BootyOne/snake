import sys
import random

import globals
from levels import easy_level, first_level, second_level, third_level
from menu import Menu
from globals import frame_color, blue, white, red, black, header_color,\
    snake_color, block_size, margin, header_margin, timer, can_move, total,\
    font, speed, lives, d_row, d_col, this_is_a_victory, snake_blocks,\
    bad_blocks, blocks_count, size, screen, draw_block, pygame, SnakeBlock
from classes import Bad_block
from save import Save
from pause import pause_menu

save = Save()
score = [save.get("Super easy"), save.get("Easy"),
         save.get("Medium"), save.get("Hard")]
game = Menu(size, score)

bad_blocks = globals.bad_blocks
_done = True
while _done:
    game.menu(screen)
    level = game.choose_difficulty(screen)
    if level == 1:
        globals.blocks_count, this_is_a_victory, \
            bad_blocks, name = first_level(bad_blocks)
        _done = False
    elif level == 2:
        font, this_is_a_victory, globals.blocks_count, \
            bad_blocks, name = second_level(bad_blocks)
        _done = False
    elif level == 4:
        _done = False
        globals.blocks_count, this_is_a_victory, name = easy_level()
    elif level == 3:
        font, this_is_a_victory, globals.blocks_count, \
            bad_blocks, name = third_level(bad_blocks)
        _done = False
    elif level == -1:
        continue


def get_random_entry_block():
    x = random.randint(1, globals.blocks_count - 1)
    y = random.randint(1, globals.blocks_count - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks or Bad_block(x, y) in bad_blocks:
        x = random.randint(1, globals.blocks_count - 1)
        y = random.randint(1, globals.blocks_count - 1)
        empty_block = SnakeBlock(x, y)
    return empty_block


font = globals.font
total = globals.total
speed = globals.speed
lives = globals.lives
snake_blocks = globals.snake_blocks
d_row = globals.d_row
can_move = globals.can_move
d_col = globals.d_col
this_is_a_victory = globals.this_is_a_victory

apple = get_random_entry_block()

while True:
    screen.fill(frame_color)
    pygame.draw.rect(screen, header_color, [0, 0, size[0], header_margin])

    text_total = font.render(f"Total: {total}", False, white)
    text_speed = font.render(f"Speed: {speed}", False, white)
    text_lives = font.render(f"Lives: {lives}", False, white)
    screen.blit(text_total, (block_size, block_size))
    screen.blit(text_lives, (blocks_count * block_size // 2, block_size))
    screen.blit(text_speed, (block_size * blocks_count -
                             text_speed.get_size()[0] // 1.6, block_size))
    for row in range(globals.blocks_count):
        for column in range(globals.blocks_count):
            if Bad_block(row, column) in bad_blocks:
                color = black
            elif (row + column) % 2 == 0:
                color = blue
            else:
                color = white
            draw_block(color, row, column)

    draw_block(red, apple.x, apple.y)

    for blocks in snake_blocks:
        draw_block(snake_color, blocks.x, blocks.y)

    pygame.display.flip()
    head = snake_blocks[-1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0 and can_move:
                d_row = -1
                d_col = 0
                can_move = False
            elif event.key == pygame.K_DOWN and d_col != 0 and can_move:
                d_row = 1
                d_col = 0
                can_move = False
            elif event.key == pygame.K_LEFT and d_row != 0 and can_move:
                d_row = 0
                d_col = -1
                can_move = False
            elif event.key == pygame.K_RIGHT and d_row != 0 and can_move:
                d_row = 0
                d_col = 1
                can_move = False
            elif event.key == pygame.K_r:
                bad_blocks.clear()
            elif event.key == pygame.K_e:
                apple = SnakeBlock(snake_blocks[-1].x + d_row,
                                   snake_blocks[-1].y + d_col)
            elif event.key == pygame.K_ESCAPE:
                timer.tick(0)
                action, snake_blocks = game.Pause(screen, snake_blocks)
                if action == 0:
                    timer.tick(3 + speed)
                if action == 1:
                    bad_blocks.clear()
                    lives = 3
                    speed = 1
                    total = 0
                    done = True
                    game.menu(screen)
                    level = game.choose_difficulty(screen)
                    snake_blocks = [SnakeBlock(0, 0),
                                    SnakeBlock(0, 1), SnakeBlock(0, 2)]
                    new_head = head = snake_blocks[-1]
                    d_row = 0
                    d_col = 1
                    globals.blocks_count, this_is_a_victory, bad_blocks,\
                        name, font = pause_menu(level, bad_blocks, font)
                    apple = get_random_entry_block()
                    done = False
                    pygame.display.flip()

    if not head.is_inside(globals.blocks_count)\
            or Bad_block(head.x, head.y) in bad_blocks:
        if name == "Super easy" and total > score[0]:
            save.save(name, total)
            score[0] = total
        if name == "Easy" and total > score[1]:
            save.save(name, total)
            score[1] = total
        if name == "Medium" and total > score[2]:
            save.save(name, total)
            score[2] = total
        if name == "Hard" and total > score[3]:
            save.save(name, total)
            score[3] = total

        game = Menu(size, score)
        bad_blocks.clear()
        lives = 3
        speed = 1
        total = 0
        done = True
        game.menu(screen)
        level = game.choose_difficulty(screen)
        snake_blocks = [SnakeBlock(0, 0),
                        SnakeBlock(0, 1), SnakeBlock(0, 2)]
        new_head = head = snake_blocks[-1]
        d_row = 0
        d_col = 1
        globals.blocks_count, this_is_a_victory, bad_blocks, name,\
            font = pause_menu(level, bad_blocks, font)
        apple = get_random_entry_block()
        done = False
        pygame.display.flip()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    can_move = True
    if new_head in snake_blocks:
        if lives:
            lives -= 1
        else:
            if name == "Super easy" and total > score[0]:
                save.save(name, total)
                score[0] = total
            if name == "Easy" and total > score[1]:
                save.save(name, total)
                score[1] = total
            if name == "Medium" and total > score[2]:
                save.save(name, total)
                score[2] = total
            if name == "Hard" and total > score[3]:
                save.save(name, total)
                score[3] = total

            game = Menu(size, score)
            bad_blocks.clear()
            lives = 3
            speed = 1
            total = 0
            done = True
            game.menu(screen)
            level = game.choose_difficulty(screen)
            snake_blocks = [SnakeBlock(0, 0),
                            SnakeBlock(0, 1), SnakeBlock(0, 2)]
            new_head = head = snake_blocks[-1]
            d_row = 0
            d_col = 1
            globals.blocks_count, this_is_a_victory, bad_blocks,\
                name, font = pause_menu(level, bad_blocks, font)
            apple = get_random_entry_block()
            done = False
            pygame.display.flip()
    if apple == head:
        total += 1
        speed = total // 5 + 1
        snake_blocks.append(apple)
        apple = get_random_entry_block()
    else:
        snake_blocks.pop(0)

    if snake_blocks.count(10) > this_is_a_victory:
        print("YOU WIN")
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)

    timer.tick(3 + speed)
