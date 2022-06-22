import copy

import pygame
import block


class Grid():
    def __init__(self, screen, a):
        self.screen = screen
        self.screen_rect_width, self.screen_rect_height = screen.get_rect().right, screen.get_rect().bottom
        self.line_color = (80, 80, 80)
        self.a = a
        self.times = self.screen_rect_height // self.a
        # self.grids = [[0 if (i % 3 == 0 or j % 3 == 0) else 1 for i in range(self.times)] for j in range(self.times)]
        self.grids = [[0 for _ in range(self.times)] for _ in range(self.times)]

    def draw(self):
        for i in range(self.times + 1):
            width = 1
            pygame.draw.line(self.screen, self.line_color, (0, i * self.a), (self.screen_rect_height, i * self.a),
                             width)
            pygame.draw.line(self.screen, self.line_color, (i * self.a, 0), (i * self.a, self.screen_rect_height),
                             width)
        for i in range(self.times):
            for j in range(self.times):
                if self.grids[i][j] == 1:
                    b = block.Block(self.screen, i * self.a, j * self.a, self.a)
                    b.draw()

    def change(self, x, y, work):
        x = int(x // self.a)
        y = int(y // self.a)
        if x < self.times and y < self.times:
            if work == 0:
                self.grids[x][y] = 0 if self.grids[x][y] == 1 else 1
            elif work == 1:
                #   最简单的稳定结构
                #       **
                #       **
                self.grids[x][y] = 1
                self.grids[(x + 1) % self.times][y] = 1
                self.grids[x][(y + 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 1) % self.times] = 1
            elif work == 2:
                #   稳定结构小船
                #       *
                #     * _ *
                #       * *
                self.grids[x][y] = 0
                self.grids[x][(y - 1) % self.times] = 1
                self.grids[(x - 1) % self.times][y] = 1
                self.grids[(x + 1) % self.times][y] = 1
                self.grids[x][(y + 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 1) % self.times] = 1
            elif work == 3:
                #   熄灭的火花线圈
                self.grids[x][y] = 0
                self.grids[(x - 3) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 3) % self.times][(y - 2) % self.times] = 1
                self.grids[(x - 2) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 2) % self.times][(y - 2) % self.times] = 1
                self.grids[(x - 3) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 3) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 1) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 1) % self.times][y] = 1
                self.grids[(x + 1) % self.times][y] = 1
                self.grids[(x - 1) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 1) % self.times] = 1
                self.grids[(x - 3) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 3) % self.times][(y + 1) % self.times] = 1
                self.grids[(x - 2) % self.times][(y + 2) % self.times] = 1
                self.grids[(x + 2) % self.times][(y + 2) % self.times] = 1
                self.grids[(x - 3) % self.times][(y + 2) % self.times] = 1
                self.grids[(x + 3) % self.times][(y + 2) % self.times] = 1
            elif work == 4:
                #   振荡器
                self.grids[x][y] = 1
                self.grids[(x - 1) % self.times][y] = 1
                self.grids[(x + 1) % self.times][y] = 1
            elif work == 5:
                #   十五项全能振荡器
                self.grids[x][y] = 1
                self.grids[(x - 1) % self.times][y] = 1
                self.grids[(x - 3) % self.times][y] = 1
                self.grids[(x - 4) % self.times][y] = 1
                self.grids[(x + 1) % self.times][y] = 1
                self.grids[(x + 2) % self.times][y] = 1
                self.grids[(x + 4) % self.times][y] = 1
                self.grids[(x + 5) % self.times][y] = 1
                self.grids[(x - 2) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 3) % self.times][(y + 1) % self.times] = 1
                self.grids[(x - 2) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 3) % self.times][(y - 1) % self.times] = 1
            elif work == 6:
                #   滑翔机
                #       *
                #       _ *
                #     * * *
                self.grids[x][y] = 0
                self.grids[x][(y - 1) % self.times] = 1
                self.grids[(x + 1) % self.times][y] = 1
                self.grids[x][(y + 1) % self.times] = 1
                self.grids[(x - 1) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 1) % self.times] = 1
            elif work == 7:
                # 飞船
                self.grids[(x - 1) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 2) % self.times][y] = 1
                self.grids[(x - 2) % self.times][(y + 1) % self.times] = 1
                self.grids[(x - 2) % self.times][(y + 2) % self.times] = 1
                self.grids[(x - 1) % self.times][(y + 2) % self.times] = 1
                self.grids[x][(y + 2) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 2) % self.times] = 1
                self.grids[(x + 2) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 2) % self.times][(y - 1) % self.times] = 1
            elif work == 8:
                # 高斯帕滑翔机枪
                self.grids[x][y] = 1
                self.grids[(x + 1) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 2) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 2) % self.times][y] = 1
                self.grids[(x + 3) % self.times][y] = 1
                self.grids[(x + 2) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 1) % self.times][(y + 2) % self.times] = 1
                self.grids[(x - 4) % self.times][y] = 1
                self.grids[(x - 4) % self.times][(y + 1) % self.times] = 1
                self.grids[(x - 4) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 3) % self.times][(y - 2) % self.times] = 1
                self.grids[(x - 3) % self.times][(y + 2) % self.times] = 1
                self.grids[(x - 2) % self.times][(y + 3) % self.times] = 1
                self.grids[(x - 1) % self.times][(y + 3) % self.times] = 1
                self.grids[(x - 2) % self.times][(y - 3) % self.times] = 1
                self.grids[(x - 1) % self.times][(y - 3) % self.times] = 1
                self.grids[(x - 13) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 13) % self.times][y] = 1
                self.grids[(x - 14) % self.times][(y - 1) % self.times] = 1
                self.grids[(x - 14) % self.times][y] = 1
                self.grids[(x + 6) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 7) % self.times][(y - 1) % self.times] = 1
                self.grids[(x + 6) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 7) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 6) % self.times][(y - 3) % self.times] = 1
                self.grids[(x + 7) % self.times][(y - 3) % self.times] = 1
                self.grids[(x + 8) % self.times][y] = 1
                self.grids[(x + 10) % self.times][y] = 1
                self.grids[(x + 10) % self.times][(y + 1) % self.times] = 1
                self.grids[(x + 8) % self.times][(y - 4) % self.times] = 1
                self.grids[(x + 10) % self.times][(y - 4) % self.times] = 1
                self.grids[(x + 10) % self.times][(y - 5) % self.times] = 1
                self.grids[(x + 20) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 20) % self.times][(y - 3) % self.times] = 1
                self.grids[(x + 21) % self.times][(y - 2) % self.times] = 1
                self.grids[(x + 21) % self.times][(y - 3) % self.times] = 1
            elif work == 9:
                #           *
                #         * _ *
                #         * * *
                #           *
                left = (x - 1) % self.times
                right = (x + 1) % self.times
                top = (y - 1) % self.times
                bottom = (y + 1) % self.times
                self.grids[x][y] = 0
                self.grids[x][top] = 1
                self.grids[left][y] = 1
                self.grids[right][y] = 1
                self.grids[left][bottom] = 1
                self.grids[x][bottom] = 1
                self.grids[right][bottom] = 1
                self.grids[x][(y + 2) % self.times] = 1


    def conway(self):
        currentGrids = copy.deepcopy(self.grids)
        for i in range(self.times):
            for j in range(self.times):
                num = 0
                left = (i - 1) % self.times
                right = (i + 1) % self.times
                top = (j - 1) % self.times
                bottom = (j + 1) % self.times
                if currentGrids[left][top] == 1:
                    num += 1
                if currentGrids[i][top] == 1:
                    num += 1
                if currentGrids[right][top] == 1:
                    num += 1
                if currentGrids[left][j] == 1:
                    num += 1
                if currentGrids[right][j] == 1:
                    num += 1
                if currentGrids[left][bottom] == 1:
                    num += 1
                if currentGrids[i][bottom] == 1:
                    num += 1
                if currentGrids[right][bottom] == 1:
                    num += 1
                if (currentGrids[i][j] == 1 and (num == 2 or num == 3)) or (currentGrids[i][j] == 0 and num == 3):
                    self.grids[i][j] = 1
                else:
                    self.grids[i][j] = 0

    def clear(self):
        for i in range(self.times):
            for j in range(self.times):
                self.grids[i][j] = 0
