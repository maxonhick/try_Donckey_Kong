import pygame

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
square.fill('Yellow')

# пол
block = pygame.image.load('images/Block.png').convert_alpha()
block_x = 60
block_y = 950
hight_block = 33
lenght_block = 70
blocks_rect = []

# stairs
stair = pygame.image.load('images/ladder4.png').convert_alpha()
stairs_rect = []
full_stairs_rect = False
stair_y = 0
stair_x = 0

# mario
mario_right = [pygame.image.load('images/mario/right/mario-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/jump-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/mario-right.png').convert_alpha(),
               pygame.image.load('images/mario/right/run-right.png').convert_alpha()]
mario_left = [pygame.image.load('images/mario/left/mario-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/jump-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/mario-left.png').convert_alpha(),
               pygame.image.load('images/mario/left/run-left.png')]
mario_climbing = [pygame.image.load('images/mario/climb/marioClimb1.png').convert_alpha(),
                  pygame.image.load('images/mario/climb/marioClimb2.png').convert_alpha()]
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
jump_count = 7

# игра продолжается
game_over = False
game_play = True

def draw_level():
    global block_x, block_y, hight_mario, hight_block, mario_y, lenght_block, is_jump, jump_count, full_stairs_rect
    blocks_rect.clear()
    for _ in range(6):
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
                        stairs_rect.append(square.get_rect(topleft=(block_x - 20, block_y - 95)))
                    screen.blit(square, (block_x - 20, block_y - 95))
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
                block_x -= 70
                if i < 4:
                    block_y -= 4
        elif _ % 2:
            for i in range(9):
                if i == 6:
                    screen.blit(stair, (block_x, block_y - 20))
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 39))
                    screen.blit(stair, (block_x, block_y - 58))
                    screen.blit(stair, (block_x, block_y - 77))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 99)))
                    screen.blit(square, (block_x, block_y - 99))
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
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 117)))
                    screen.blit(square, (block_x, block_y - 117))
                elif _ == 3 and i == 5:
                    screen.blit(stair, (block_x + 50, block_y - 20))
                    screen.blit(block, (block_x , block_y))
                    screen.blit(stair, (block_x + 50, block_y - 39))
                    screen.blit(stair, (block_x + 50, block_y - 58))
                    screen.blit(stair, (block_x + 50, block_y - 77))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x + 50, block_y - 107)))
                    screen.blit(square, (block_x + 50, block_y - 107))
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
                        stairs_rect.append(square.get_rect(topleft=(block_x - 20, block_y - 95)))
                    screen.blit(square, (block_x - 20, block_y - 95))
                elif _ == 2 and i == 4:
                    screen.blit(block, (block_x, block_y))
                    screen.blit(stair, (block_x, block_y - 19))
                    screen.blit(stair, (block_x, block_y - 35))
                    screen.blit(stair, (block_x, block_y - 54))
                    screen.blit(stair, (block_x, block_y - 73))
                    screen.blit(stair, (block_x, block_y - 92))
                    if not full_stairs_rect:
                        stairs_rect.append(square.get_rect(topleft=(block_x, block_y - 115)))
                    screen.blit(square, (block_x, block_y - 115))
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

while not game_over:

    screen.fill((0, 0, 0))
    draw_level()
    block_x = 60
    block_y = 950

    if game_play:

        keys = pygame.key.get_pressed()

        if not mario_climb:
            if right:
                screen.blit(mario_right[walking_stage], (mario_x, mario_y))
            else:
                screen.blit(mario_left[walking_stage], (mario_x, mario_y))
            mario_rect = mario_right[0].get_rect(topleft=(mario_x, mario_y))

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
            screen.blit(mario_climbing[climbing_stage], (stair_x, mario_y))
            print(climbing_stage)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    clock.tick(13)

pygame.quit()