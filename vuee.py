import pygame
import sys
from Cashflow import  cashflow
from datetime import datetime
import AF_by_chapter1
import  chapter1
import chapter2and3
import  chapter4
import  chapter5
import  numpy
import scipy
import math
import matplotlib
import random
import pandas
import sympy
import tkinter

# 初始化Pygame
pygame.init()

# 定义界面尺寸
screen_width = 800
screen_height = 600

# 创建界面
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("cmkallj")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# 定义字体
font = pygame.font.Font(None, 36)

# 定义按钮
button_width = 200
button_height = 50
button_x = screen_width // 2 - button_width // 2
button_y = screen_height // 2 - button_height // 2

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# 定义菜单选项
menu_options = ["choice1", "choice2", "choice3"]
menu_x = 20
menu_y = 20
menu_spacing = 40

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                # 按钮被点击，执行按钮函数
                print("inter")
            else:
                # 检查菜单选项是否被点击
                for i, option in enumerate(menu_options):
                    option_rect = pygame.Rect(
                        menu_x,
                        menu_y + i * menu_spacing,
                        font.size(option)[0],
                        font.size(option)[1]
                    )
                    if option_rect.collidepoint(mouse_pos):
                        # 菜单选项被点击，执行对应函数
                        print(f"菜单选项 {option} 被点击")

    # 渲染界面
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)
    button_text = font.render("menu", True, BLACK)
    screen.blit(button_text, (button_x + 50, button_y + 10))

    for i, option in enumerate(menu_options):
        option_text = font.render(option, True, BLACK)
        screen.blit(option_text, (menu_x, menu_y + i * menu_spacing))

    # 更新界面
    pygame.display.flip()
