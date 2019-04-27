#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: maze.py
@time: 2019/4/22 09:47
"""
import sys
import pygame
import numpy as np
import math
from queue import PriorityQueue
from stack import Stack

# define some maze flag
ROAD_VALUE = 0
ROAD_COLOR = (255, 255, 255)    # 白色
OBSTACK_VALUE = 1
OBSTACK_COLOR = (192, 192, 192)  # 灰色
BLUEROAD_VALUE = 2
BLUEROAD_COLOR = (0, 0, 255)    # 蓝色
BLUEROAD_COST = 2
YELLOWROAD_VALUE = 3
YELLOWROAD_COLOR = (255, 255, 0)  # 黄色
YELLOWROAD_COST = 4

OPTIMAL_ROAD_COLOR = (255, 0, 0)  # 红色


class Maze(object):
    def __init__(self, maze_type="maze1", start=(3, 8), target=(14, 9), start_text="S", target_text="T", grid_size=25):
        # build maze
        if maze_type == "maze1":
            self.maze = self._load_maze1()
        elif maze_type == "maze2":
            self.maze = self._load_maze2()
        else:
            raise Exception("not supported maze type")
        # horizontal grid number and vertical grid number
        self.M, self.N = self.maze.shape[1], self.maze.shape[0]
        # grid size
        self.grid_size = grid_size
        # total maze width and height
        self.width = self.grid_size * self.M
        self.height = self.grid_size * self.N

        # init screen (the maze is draw on)
        self.screen = self._init_screen(screen_size=(int(self.width + 0.2*self.width), self.height))

        # for  start and end
        self.start = start
        self.target = target
        self.start_text = start_text
        self.target_text = target_text

        # draw the maze
        self._draw()

    def _init_screen(self, screen_size=(640, 480), bg_color=(0, 0, 0)):
        """
        init pygame screen
        :param screen_size: the screen size.
        :param bg_color: background color, default is black.
        :return:
        """
        # pygame  初始化
        pygame.init()
        # 创建一个指定大小的窗口
        screen = pygame.display.set_mode(screen_size)
        # set title
        pygame.display.set_caption("A* algorithm display")
        # set bg color
        screen.fill(bg_color)
        return screen

    def _load_maze1(self):
        """load maze from array"""
        maze = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        return maze

    def _load_maze2(self):
        """load maze from array"""
        maze = np.array([
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3],
            [1,  1,  1,  1,  1, 1, 0, 1, 1,  1,  1,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 1,  1,  1,  1, 1, 1,  0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0],
            [0, 0, 1,  0,  0, 1, 0, 1,  0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1,  1,  1,  1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        return maze

    def _draw(self):
        """draw the maze."""
        # 左上角是原点，右方向是x轴，下方向是y轴, 在maze矩阵中索引用(y, x)
        for y in range(0, self.N):
            for x in range(0, self.M):
                if self.maze[y][x] == ROAD_VALUE:
                    # Surface, color, Rect, width=0 (填充格子)
                    self._fill_a_grid(x, y, ROAD_COLOR)
                elif self.maze[y][x] == OBSTACK_VALUE:
                    # Surface, color, Rect, width=0 (填充格子)
                    self._fill_a_grid(x, y, OBSTACK_COLOR)
                elif self.maze[y][x] == YELLOWROAD_VALUE:
                    self._fill_a_grid(x, y, YELLOWROAD_COLOR)
                elif self.maze[y][x] == BLUEROAD_VALUE:
                    self._fill_a_grid(x, y, BLUEROAD_COLOR)
        # draw start and end flag
        self._draw_grid_text(self.start_text, self.start[0], self.start[1])
        self._draw_grid_text(self.target_text, self.target[0], self.target[1])
        # 重画屏幕
        pygame.display.flip()

    def _draw_side_text(self, text, text_color=(255, 255, 255)):
        """draw text on side.
        :param text:
        :param x:
        :param y:
        :param text_color: 默认白色字体
        :return:
        """
        # create font
        font = pygame.font.SysFont('microsoft Yahei', int(self.grid_size * 0.8))
        # 根据字体去创建显示对象
        surface = font.render(text, False, text_color)
        # 将内容添加到相应的右边中间
        self.screen.blit(surface, (self.width + 0.2*self.width*0.1, self.height/2))
        # 重画屏幕
        # pygame.display.flip()

    def _draw_grid_text(self, text, x, y, text_color=(0, 0, 0)):
        """
         draw a text in a grid.
        :param text:
        :param x: the grid x index , [0, M)
        :param y: the grid y index, [0, N)
        :param text_color:
        :return:
        """
        # create font
        font = pygame.font.SysFont('microsoft Yahei', int(self.grid_size*0.8))
        # 根据字体去创建显示对象
        surface = font.render(text, False, text_color)
        # 将内容添加到相应的格子中间
        self.screen.blit(surface, (x*self.grid_size + self.grid_size/3, y*self.grid_size+self.grid_size/3))
        # 重画屏幕
        # pygame.display.flip()

    def _fill_a_grid(self, x, y, color, width=0):
        """fill a grid
        :param x: the column number
        :param y: the row number
        :param color:
        :param width:if 0 is fill a grad, else 1 to  draw a grid with line
        :return:
        """
        assert 0 <= x < self.M and 0 <= y < self.N
        # Surface, color, Rect, width=0 (填充格子，留出1像素的空白)
        pygame.draw.rect(self.screen, color,
                         ((x*self.grid_size+1, y*self.grid_size+1), (self.grid_size-1, self.grid_size-1)), width)

    # algorithm below
    def search(self):
        """A* algorithm to search.
        ---------
        用一个优先级队列保存当前结点和所花费的代价，每次扩展代价最小的那个，直至找到目标结点。
        """
        print("A* algorithm begin.....")
        # 起点和终点相同, self.start and self.target，直接返回
        if self.start == self.target:
            return True
        myqueue = PriorityQueue()
        cur_pos = self.start
        cur_cost = 0.  # 已花费的代价
        heu_cost = self._get_heuristic_cost(cur_pos)  # 启发式代价
        # 将起点加入到优先级队列中(总共代价，已花费代价，位置坐标，父结点位置坐标)
        myqueue.put((cur_cost+heu_cost, cur_cost, cur_pos, cur_pos))
        # 记录已经访问的点, cur_pos: par_pos
        explored = {}
        while myqueue.qsize() != 0:
            # 从优先级队列中取出一个值
            total_cost, cur_cost, cur_pos, par_pos = myqueue.get()
            # 标记该节点为已访问，并记录父结点
            if cur_pos not in explored.keys():
                explored[cur_pos] = par_pos
                # print(total_cost, cur_cost, cur_pos)
            else:
                continue  # 相当于剪枝了
            # 记录扩展的结点
            # print(total_cost, cur_cost, cur_pos)
            if cur_pos == self.target:
                print("find path, total cost is: {}".format(cur_cost))
                break
            # run a step
            for dir in ["U", "D", "L", "R", "LU", "RU", "LD", "RD"]:
                res_pos, res_cost = self._run(cur_pos, d=dir)
                if self._reachable(res_pos[0], res_pos[1]) and res_pos not in explored:
                    tmp_cost = cur_cost + res_cost + self._get_terrain_cost(res_pos)
                    heuristic_cost = self._get_heuristic_cost(res_pos)
                    # 添加到优先级队列
                    myqueue.put((heuristic_cost + tmp_cost, tmp_cost, res_pos, cur_pos))
        print("A* algorithm search done!")
        # draw the optimal path
        print("print the optimal path: ")
        parent = self.target
        while parent != self.start:
            parent = explored[parent]
            if parent != self.start:
                print(parent)
                # self._fill_a_grid(parent[0], parent[1], OPTIMAL_ROAD_COLOR)
                self._draw_grid_text("#", parent[0], parent[1], text_color=(0, 0, 0))
        # draw the optimal cost
        self._draw_side_text("cost: {}".format(round(cur_cost, 3)))
        # 重画屏幕
        pygame.display.flip()

    def _run(self, position, d="L"):
        """from position run a step follow direction d."""
        x, y = position
        cost = 0
        if d == "U":
            y = y - 1
            cost = 1
        elif d == "D":
            y = y + 1
            cost = 1
        elif d == "L":
            x = x - 1
            cost = 1
        elif d == "R":
            x = x + 1
            cost = 1
        elif d == "LU":
            x = x - 1
            y = y - 1
            cost = math.sqrt(2)
        elif d == "RU":
            x = x + 1
            y = y - 1
            cost = math.sqrt(2)
        elif d == "LD":
            x = x - 1
            y = y + 1
            cost = math.sqrt(2)
        elif d == "RD":
            x = x + 1
            y = y + 1
            cost = math.sqrt(2)
        else:
            raise Exception("not supported direction!")
        return (x, y), cost

    def _get_terrain_cost(self, position):
        """根据坐标位置得到地形代价"""
        x, y = position
        if self.maze[y][x] == ROAD_VALUE:
            return 0
        elif self.maze[y][x] == YELLOWROAD_VALUE:
            return YELLOWROAD_COST
        elif self.maze[y][x] == BLUEROAD_VALUE:
            return BLUEROAD_COST
        else:
            raise Exception("not supported terrain!")

    def _get_heuristic_cost(self, position):
        """计算position和目的点target的启发式代价"""
        x, y = position
        x0, y0 = self.target
        side_len = min(abs(x-x0), abs(y-y0))
        straight_len = max(abs(x-x0), abs(y-y0)) - side_len
        return side_len*math.sqrt(2) + straight_len * 1

    def _reachable(self, x, y):
        """check position (x,y) is reachable..."""
        return 0 <= x < self.M and 0 <= y < self.N and self.maze[y][x] != OBSTACK_VALUE

def exp1():
    maze = Maze(maze_type="maze1", start=(3, 8), target=(14, 9))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_s]:
                maze.search()
def exp2():
    maze = Maze(maze_type="maze2", start=(4, 10), target=(35, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_s]:
                maze.search()


if __name__ == "__main__":
    exp2()
