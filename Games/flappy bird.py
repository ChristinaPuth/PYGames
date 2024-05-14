
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the window size
WIN_WIDTH = 400
WIN_HEIGHT = 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW=(255, 255, 0)
RED=(255, 0, 0)

# set font
font = pygame.font.Font(None, 36)

# Setting birdie parameters
bird_width = 40
bird_height = 30
bird_x = 50
bird_y = WIN_HEIGHT // 2
gravity = 0.25
jump = -7
bird_velocity = 0
score = 0

# Setting pipeline parameters
pipe_width = 50
pipe_gap = 200
pipe_velocity = 3
pipe_list = []

#Loading the bird image
bird_img = pygame.image.load('/Users/pusi/PycharmProjects/PYGames1/Games/bird.png').convert_alpha()
bird_img = pygame.transform.scale(bird_img, (bird_width, bird_height))

# 加载管道图片
pipe_img = pygame.image.load('/Users/pusi/PycharmProjects/PYGames1/Games/pipe.png').convert_alpha()
pipe_img = pygame.transform.scale(pipe_img, (pipe_width, WIN_HEIGHT))

# 创建管道
def create_pipe():
    random_pos = random.randint(150, 400)
    top_pipe = pipe_img.get_rect(midbottom=(500, random_pos - pipe_gap // 2))
    bottom_pipe = pipe_img.get_rect(midtop=(500, random_pos + pipe_gap // 2))
    return top_pipe, bottom_pipe

# 碰撞检测
def check_collision():
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            return True
    if bird_y >= WIN_HEIGHT or bird_y <= 0:
        return True
    return False

# 显示游戏结束提示消息
def show_message(text):
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
    win.blit(text_surface, text_rect)
    pygame.display.update()

# 主循环
def main():
    global bird_y, bird_velocity, pipe_list, bird_rect, score

    clock = pygame.time.Clock()

    while True:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump

        # 初始化管道列表
        if not pipe_list:
            pipe_list.extend(create_pipe())

        # 移动小鸟
        bird_velocity += gravity
        bird_y += bird_velocity
        bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

        # 移动管道
        for pipe in pipe_list:
            pipe.centerx -= pipe_velocity

        # 生成新的管道
        if pipe_list[-1].centerx < 200:
            pipe_list.extend(create_pipe())
            # 每过一次管道得到10分
            score += 10

        # 移除超出屏幕的管道
        if pipe_list[0].right < 0:
            del pipe_list[0]
            del pipe_list[0]

        # 清空屏幕
        win.fill(BLACK)

        # 画管道
        for pipe in pipe_list:
            if pipe.bottom >= WIN_HEIGHT:
                win.blit(pipe_img, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_img, False, True)
                win.blit(flip_pipe, pipe)

        # 画小鸟
        win.blit(bird_img, (bird_x, bird_y))

        # 碰撞检测
        if check_collision():
            show_message(f"You Lost! Your score: {score}")
            pygame.time.delay(2000)  # 显示消息 2 秒钟
            return

        # 显示分数
        score_text = font.render(f"Score: {score}", True, YELLOW)
        win.blit(score_text, (10, 10))

        # 更新屏幕
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
