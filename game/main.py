import pygame
import random

clock = pygame.time.Clock()

# высота и ширина лестницы 20
# высота марио 36 ширина 24

pygame.init()

# настройки экрана
screen_weight = 820
screen_hight = 1170
screen = pygame.display.set_mode((screen_weight, screen_hight))
pygame.display.set_caption('Donckey Kong')

square = pygame.Surface((20, 85))

# fonts and label
font = pygame.font.Font('fonts/OpenSans-Italic-VariableFont_wdth,wght.ttf', 40)
lose_label = font.render('Игра окончена', False, 'Red')
restart_label = font.render('Попробовать снова', False, (63, 137, 205))
restart_label_rect = restart_label.get_rect(topleft=(230, 600))
win_label = font.render('Игра пройдена', False, 'Red')
try_again_label = font.render('Повторишь свой успех?', False, (63, 137, 205))
try_again_label_rect = try_again_label.get_rect(topleft=(210, 600))

# пол
block = pygame.image.load('images/Block.png').convert_alpha()
block_x = 60
block_y = 950
hight_block = 33
lenght_block = 70
blocks_rect = []
last_level_x = 200
last_level_y = 260

# stairs
stair = pygame.image.load('images/ladder4.png').convert_alpha()
stairs_rect = []
full_stairs_rect = False
stair_y = 0
stair_x = 0

# barrels
barrels_stack = pygame.image.load('images/barrel/barrel-stack.png').convert_alpha()
Kong_Timer = pygame.USEREVENT + 1
Last_Kong_Timer = pygame.USEREVENT + 1
barrel_timer = pygame.USEREVENT + 1
barrel_go_down = pygame.image.load('images/barrel/barrel-down.png').convert_alpha()
barrel = [pygame.image.load('images/barrel/barrel1.png').convert_alpha(),
          pygame.image.load('images/barrel/barrel2.png').convert_alpha(),
          pygame.image.load('images/barrel/barrel3.png').convert_alpha(),
          pygame.image.load('images/barrel/barrel4.png').convert_alpha()
          ]
barrels = []
start_barrel_x = 248
start_barrel_y = 350
pygame.time.set_timer(Kong_Timer, 3500)

# mario
mario_right = [pygame.image.load('images/mario/right/mario-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/jump-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/mario-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/run-right.png').convert_alpha()
               ]
mario_left = [pygame.image.load('images/mario/left/mario-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/jump-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/mario-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/run-left.png')
               ]
mario_climbing = [pygame.image.load('images/mario/climb/marioClimb1.png').convert_alpha(),
                  pygame.image.load('images/mario/climb/marioClimb2.png').convert_alpha()
                  ]
hight_mario = 36
weight_mario = 24
mario_speed_x = 7
mario_speed_y = 7
mario_x = 180
mario_y = block_y - 40
walking_stage = 0
climbing_stage = 0
mario_climb = False
right = True
is_jump = False
last_block_y = block_y
is_on_block_mario = False
on_different_block = False
jump_count = 7

# Donckey Kong
dk_throw = [pygame.image.load('images/dk/dkLeft.png').convert_alpha(),
            pygame.image.load('images/dk/dkRight.png').convert_alpha()
            ]
dk_stand = pygame.image.load('images/dk/dkStand.png').convert_alpha()
dk_x = 120
dk_y = 282
throw_animation = 1
number_timer = 0

# queen
queen = pygame.image.load('images/queen/queen1.png').convert_alpha()
queen_x = 235
queen_y = 208

# игра продолжается
game_over = False
game_play = True

def draw_level():
    global last_level_x, last_level_y, block_x, block_y, hight_mario, hight_block, mario_y, lenght_block, is_jump, jump_count, full_stairs_rect
    blocks_rect.clear()
    for _ in range(7):
        if _ == 0:
            for i in range(10):
                if i == 4:
                    screen.blit(stair, (block_x - 20, block_y - 20))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x - 20, block_y - 38))
                    screen.blit(stair, (block_x - 20, block_y - 90))
                elif i == 8:
                    screen.blit(stair, (block_x - 20, block_y - 16))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x - 20, block_y - 35))
                    screen.blit(stair, (block_x - 20, block_y - 54))
                    screen.blit(stair, (block_x - 20, block_y - 73))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x - 20, block_y - 94)))
                else:
                    screen.blit(block, (block_x, block_y))
                blocks_rect.append(block.get_rect(topleft=(block_x, block_y)))
                block_x += 70
                if i >= 5:
                    block_y -= 4
            block_y -= (hight_mario + hight_block + 10)
            block_x -= 140
        elif _ == 5:
            for i in range(9):
                blocks_rect.append(block.get_rect(topleft=(block_x, block_y)))
                screen.blit(block, (block_x, block_y))
                if i == 8:
                    screen.blit(barrels_stack, (block_x, block_y - 80))
                block_x -= 70
                if i < 4:
                    block_y -= 4
        elif _ == 6:
            for i in range(3):
                blocks_rect.append(block.get_rect(topleft=(last_level_x, last_level_y)))
                if i == 2:
                    screen.blit(stair, (last_level_x + 50, last_level_y))
                    screen.blit(stair, (last_level_x + 50, last_level_y + 19))
                    screen.blit(stair, (last_level_x + 50, last_level_y + 38))
                    screen.blit(stair, (last_level_x + 50, last_level_y + 57))
                    screen.blit(stair, (last_level_x + 50, last_level_y + 76))
                    screen.blit(stair, (last_level_x + 50, last_level_y + 95))
                if not full_stairs_rect:
                    stairs_rect.append(square.get_rect(topleft=(last_level_x + 50, last_level_y - 4)))
                screen.blit(block, (last_level_x, last_level_y))
                last_level_x += 70
        elif _ % 2:
            for i in range(9):
                if i == 6:
                    screen.blit(stair, (block_x, block_y - 20))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 39))
                    screen.blit(stair, (block_x, block_y - 58))
                    screen.blit(stair, (block_x, block_y - 77))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 98)))
                elif _ == 3 and i == 2:
                    screen.blit(stair, (block_x + 50, block_y - 20))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x + 50, block_y - 80))
                    screen.blit(stair, (block_x + 50, block_y - 99))
                elif _ == 1 and i == 4:
                    screen.blit(stair, (block_x, block_y - 20))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 39))
                    screen.blit(stair, (block_x, block_y - 58))
                    screen.blit(stair, (block_x, block_y - 77))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 116)))
                elif _ == 3 and i == 5:
                    screen.blit(stair, (block_x + 50, block_y - 20))
                    screen.blit(block, (block_x , block_y))
                    screen.blit(stair, (block_x + 50, block_y - 39))
                    screen.blit(stair, (block_x + 50, block_y - 58))
                    screen.blit(stair, (block_x + 50, block_y - 77))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x + 50, block_y - 106)))
                else:
                    screen.blit(block, (block_x, block_y))
                blocks_rect.append(block.get_rect(topleft=(block_x, block_y)))
                block_x -= 70
                block_y -= 4
            block_x += 140
            block_y -= (hight_mario + hight_block + 10)
        else:
            for i in range(9):
                if i == 7:
                    screen.blit(stair, (block_x - 20, block_y - 16))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x - 20, block_y - 35))
                    screen.blit(stair, (block_x - 20, block_y - 54))
                    screen.blit(stair, (block_x - 20, block_y - 73))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x - 20, block_y - 94)))
                elif _ == 2 and i == 4:
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 19))
                    screen.blit(stair, (block_x, block_y - 35))
                    screen.blit(stair, (block_x, block_y - 54))
                    screen.blit(stair, (block_x, block_y - 73))
                    screen.blit(stair, (block_x, block_y - 92))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 114)))
                elif _ == 2 and i == 2:
                    screen.blit(stair, (block_x, block_y - 19))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 38))
                    screen.blit(stair, (block_x, block_y - 81))
                    screen.blit(stair, (block_x, block_y - 100))
                elif _ == 4 and i == 3:
                    screen.blit(stair, (block_x + 50, block_y - 19))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x + 50, block_y - 38))
                    screen.blit(stair, (block_x + 50, block_y - 81))
                    screen.blit(stair, (block_x + 50, block_y - 100))
                else:
                    screen.blit(block, (block_x, block_y))
                blocks_rect.append(block.get_rect(topleft=(block_x, block_y)))
                block_x += 70
                block_y -= 4
            block_x -= 140
            block_y -= (hight_mario + hight_block + 10)
    full_stairs_rect = True
    last_level_x = 200
    screen.blit(queen, (queen_x, queen_y))

def barrel_collapsed_stair(el):
    rect = el[0]
    last_stair_rect = el[5]
    for stair in stairs_rect:
        if rect.colliderect(stair) and rect.y < stair.y and last_stair_rect != stair:
            rect.x = stair.x
            el[5] = stair
            return True
    return False

def barrel_on_block(rect):
    global blocks_rect, lenght_block
    for block in blocks_rect:
        if rect[7] :
            if block.x - 29 <= rect[0].x <= block.x + lenght_block:
                if -8 <= block.y - rect[0].y - 24 <= 5 and rect[6].y - block.y <= -25:
                    rect[6] = block
                    rect[7] = False
                    rect[0].y = block.y - 24
                    rect[3] = False
                    return True
        else:
            if block.x - 29 <= rect[0].x <= block.x + lenght_block:
                if -8 <= block.y - rect[0].y - 24 <= 5:
                    rect[6] = block
                    rect[0].y = block.y - 24
                    rect[3] = False
                    return True
    if not rect[3]:
        rect[3] = True
        rect[1] = not rect[1]
    return False

def draw_barrels():
    global screen_hight, game_play
    for (i, el) in enumerate(barrels):
        if el[0].x > 820 or el[0].x < - 29 or el[0].y > screen_hight:
            barrels.pop(i)
        else:
            if mario_rect.colliderect(el[0]):
                game_play = False
            
            if el[4]:
                if not barrel_on_block(el):
                    el[2] = 0
                    screen.blit(barrel_go_down, el[0])
                    el[0].y += 10
                else:
                    el[4] = False
                    screen.blit(barrel[el[2]], el[0])
                    el[2] += 1
                    if el[2] == 4:
                        el[2] = 0

                    if el[1]:
                        el[0].x += 10
                    else:
                        el[0].x -= 10
            else:
                if barrel_collapsed_stair(el):
                    el[7] = random.randint(0, 1)
                    if el[7]: 
                        el[4] = True
                        el[2] = 0
                        screen.blit(barrel_go_down, el[0])
                        el[0].y += 10
                    else:
                        screen.blit(barrel[el[2]], el[0])
                        el[2] += 1
                        if el[2] == 4:
                            el[2] = 0

                        if el[1]:
                            el[0].x += 10
                        else:
                            el[0].x -= 10
                else:
                    if not barrel_on_block(el):
                        el[2] = 0
                        screen.blit(barrel_go_down, el[0])
                        el[0].y += 10
                    else:
                        screen.blit(barrel[el[2]], el[0])
                        el[2] += 1
                        if el[2] == 4:
                            el[2] = 0

                        if el[1]:
                            el[0].x += 10
                        else:
                            el[0].x -= 10

def check_stairs():
    for stair in stairs_rect:
        if mario_rect.colliderect(stair):
            return (True, stair.y, stair.x)
    return (False, 0, 0)

def on_block_mario():
    global mario_y, mario_x, is_jump, jump_count, is_on_block_mario, last_block_y
    is_on_block_mario = False
    for block in blocks_rect:
        if block.x <= mario_x <= block.x + lenght_block:
            if -15 <= block.y - mario_y - hight_mario <= 5:
                mario_y = block.y - hight_mario
                if last_block_y != block.y:
                    is_jump = False
                    jump_count = 7
                last_block_y = block.y
                is_on_block_mario = True

def mario_on_different_block():
    global is_on_block_mario, on_different_block, last_block_y, mario_x, hight_mario, lenght_block
    on_different_block = False
    for block in blocks_rect:
        if block.x <= mario_x <= block.x + lenght_block:
            if -15 <= block.y - mario_y - hight_mario <= 5:
                is_on_block_mario = True
                if last_block_y != block.y:
                    on_different_block = True
                last_block_y = block.y

def mario_win():
    if mario_rect.y < 230 and not is_jump and is_on_block_mario:
        return True
    else:
        return False

while not game_over:

    mario_rect = mario_right[0].get_rect(topleft=(mario_x, mario_y))
    screen.fill((0, 0, 0))
    draw_level()
    draw_barrels()
    block_x = 60
    block_y = 950

    events = pygame.event.get() 

    if mario_win():
        screen.fill('Black')
        screen.blit(win_label, (280, 520))
        screen.blit(try_again_label, try_again_label_rect)
        pygame.time.set_timer(Kong_Timer, 0)
        barrels.clear()

        mouse = pygame.mouse.get_pos()
        if try_again_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            walking_stage = 0
            climbing_stage = 0
            number_timer = 0
            game_play = True
            mario_climb = False
            right = True
            is_jump = False
            last_block_y = block_y
            is_on_block_mario = False
            on_different_block = False
            mario_x = 180
            mario_y = block_y - 40
            pygame.time.set_timer(Kong_Timer, 3500)
    elif game_play:

        keys = pygame.key.get_pressed()

        if number_timer == 0:
            screen.blit(dk_stand, (dk_x, dk_y))
        elif number_timer == 1:
            screen.blit(dk_throw[0], (dk_x, dk_y))
        elif number_timer == 2:
            screen.blit(dk_throw[1], (dk_x, dk_y))

        if not mario_climb:
            if right:
                screen.blit(mario_right[walking_stage], (mario_x, mario_y))
            else:
                screen.blit(mario_left[walking_stage], (mario_x, mario_y))

            if keys[pygame.K_LEFT]:
                mario_x -= mario_speed_x
                if right:
                    walking_stage = 0
                    right = False
                else:
                    walking_stage += 1
                if mario_x < 0:
                    mario_x = 0
            elif keys[pygame.K_RIGHT]:
                mario_x += mario_speed_x
                if right:
                    walking_stage += 1
                else:
                    walking_stage = 0
                    right = True
                if mario_x > screen_weight - weight_mario:
                    mario_x = screen_weight - weight_mario
            elif keys[pygame.K_UP]:
                flag, stair_y, stair_x = check_stairs()
                if flag:
                    walking_stage = 0
                    mario_climb = True
            elif keys[pygame.K_DOWN]:
                flag, stair_y, stair_x = check_stairs()
                if flag:
                    walking_stage = 0
                    mario_climb = True

            on_block_mario()
            if not is_on_block_mario and not is_jump:
                mario_y += 10

            if not is_jump:
                if keys[pygame.K_SPACE]:               
                    is_jump = True
            else:
                if jump_count >= -7:
                    if jump_count > 0:
                        mario_y -= (jump_count)**2 / 2
                    else:
                        mario_y += (jump_count)**2 / 2

                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 7
                
            if walking_stage == 4:
                walking_stage = 0
        else:
            if keys[pygame.K_UP]:
                climbing_stage += 1
                if climbing_stage == 2:
                    climbing_stage = 0
                if mario_y > stair_y - hight_mario:
                    mario_y -= mario_speed_y
                else:
                    mario_climb = False
                    climbing_stage = 0
            elif keys[pygame.K_DOWN] and mario_y - stair_y < 85:
                climbing_stage += 1
                if climbing_stage == 2:
                    climbing_stage = 0
                mario_on_different_block()
                if on_different_block:
                    mario_climb = False
                    climbing_stage = 0
                elif is_on_block_mario and mario_y - stair_y > 0:
                    mario_climb = False
                    climbing_stage = 0
                else:
                    mario_y += mario_speed_y
            screen.blit(mario_climbing[climbing_stage], (stair_x, mario_y))
    else:
        screen.fill('Black')
        screen.blit(lose_label, (280, 520))
        screen.blit(restart_label, restart_label_rect)
        pygame.time.set_timer(Kong_Timer, 0)
        barrels.clear()
        mario_x = 180
        mario_y = block_y - 40

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            walking_stage = 0
            climbing_stage = 0
            number_timer = 0
            game_play = True
            mario_climb = False
            right = True
            is_jump = False
            last_block_y = block_y
            is_on_block_mario = False
            on_different_block = False
            pygame.time.set_timer(Kong_Timer, 3500)
    
    for event in events:
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == Kong_Timer and number_timer == 0:
            number_timer = 1
            pygame.time.set_timer(Kong_Timer, 3500)
            pygame.time.set_timer(barrel_timer, 1000)
        elif event.type == barrel_timer and number_timer == 1:
            if [barrel[0].get_rect(topleft=(start_barrel_x, start_barrel_y)), True, 0, False, False, None, barrel[0].get_rect(topleft=(start_barrel_x, start_barrel_y)), False] in barrels:
                continue
            else:
                number_timer = 2
                pygame.time.set_timer(barrel_timer, 3500)
                pygame.time.set_timer(Last_Kong_Timer, 1000)
                barrels.append([barrel[0].get_rect(topleft=(start_barrel_x, start_barrel_y)), True, 0, False, False, None, barrel[0].get_rect(topleft=(start_barrel_x, start_barrel_y)), False])
            # 0 barrel_rect,1 right,2 animation stage,3 is_changed_right,4 is barrel on stair,5 last stair rect,6 last block rect, 7 go down on stair
        elif event.type == Last_Kong_Timer and number_timer == 2:
            pygame.time.set_timer(Last_Kong_Timer, 1000)
            number_timer = 0
    
    pygame.display.update()
    
    clock.tick(13)

pygame.quit()