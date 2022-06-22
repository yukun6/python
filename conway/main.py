import pygame
import sys
import setting
import button, grid

COLOR_BUTTON = (29, 191, 152)
COLOR_BIT_BUTTON = (200, 20, 20)
button_number = 15
simsun = r"E:\code\python\studyauto\conway\font\simsun.ttc"


def run():
    pygame.init()
    settings = setting.Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    g = grid.Grid(screen, 10)
    pygame.display.set_caption("CONWAY")
    butt = []
    text = ''
    for i in range(button_number):
        if i == 0:
            text = '默认'
        elif i == 1:
            text = '最简单的稳定结构'
        elif i == 2:
            text = '小船结构'
        elif i == 3:
            text = '熄灭的火花线圈'
        elif i == 4:
            text = '简易振荡器'
        elif i == 5:
            text = '十五项全能振荡器'
        elif i == 6:
            text = '滑翔机'
        elif i == 7:
            text = '水平运动飞船'
        elif i == 8:
            text = '高斯帕滑翔机枪'
        elif i == 9:
            text = '菱形变换结构'
        elif i == button_number - 1:
            text = '清空'
        else:
            text = ''
        butt.append(
            button.Button(screen, 820, 5 + i * 50, 200, 45, 1, COLOR_BUTTON, COLOR_BIT_BUTTON, simsun, 24, text))
    fClock = pygame.time.Clock()
    fps = 60
    flag = 0  # 标记速度
    pause = 0  # 开始暂停
    work = 0  # 标记鼠标使用的是什么图案

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = 1 if pause == 0 else 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                g.change(x, y, work)
                for i in range(button_number):
                    if butt[i].check_click((x, y)):
                        work = i
                        break
        screen.fill(settings.bg_color)
        g.draw()
        if work == button_number - 1:
            g.clear()
        if flag % (fps / 10) == 0 and pause == 0:
            g.conway()
        for i in range(button_number):
            butt[i].draw_button()
            butt[i].draw_text()
        pygame.display.flip()
        fClock.tick(fps)
        flag += 1


run()
