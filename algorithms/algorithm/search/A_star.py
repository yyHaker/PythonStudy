import numpy as np

maze = np.mat("""[
            1 1 1 1 1 1 1 1 1 1 1;
            1 0 1 0 0 0 0 1 0 0 1;
            1 0 1 0 1 1 0 1 0 1 1;
            1 0 0 0 0 0 1 0 0 0 1;
            1 1 1 1 1 0 1 1 0 1 1;
            1 0 0 0 0 0 1 1 1 0 1;
            1 1 1 0 1 1 1 0 0 0 1;
            1 0 0 0 1 0 0 0 0 1 1;
            1 0 1 0 0 0 1 1 0 0 1;
            1 1 1 1 1 1 1 1 1 1 1]""",dtype=np.int8)

dire=[(0,1),(1,0),(0,-1),(-1,0)]

def mark(maze,pos):
    maze[pos[0],pos[1]]=2

def passable(maze,pos):
    return maze[pos[0],pos[1]]==0

def find_path(maze,pos,end):
    mark(maze,pos) #标记
    if pos==end:
        #走到终点或者开始点就是终点
        print(pos, end=' ')
        return True
    for i in range(4):
        nextp=(pos[0]+dire[i][0], pos[1]+dire[i][1])
        #探索每一个可能性
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                #递归开始，如果这样一直递归下去递归到终点
                print(pos, end='  ')
                #输出结果
                return True
    return False


def st_find(maze, start, end):
    """maze为迷宫矩阵，start和end是开始点和结束点
    返回一个list"""

    if start == end:
        # 特殊情况，起点就是终点
        return [(start, 0)]
    st = []  # stack的缩写，表示栈
    mark(maze, start)
    st.append((start, 0))
    # 将开始位置和要探索的未知位置压入栈
    while len(st) != 0:
        # 只要还有没有探索完的地方就不会结束
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = (pos[0] + dire[i][0], pos[1] + dire[i][1])
            # 下一个探查点
            if passable(maze, nextp):
                st.append((pos, i + 1))
                # 如果可行，把下一个没探测的点压入栈
                mark(maze, nextp)
                st.append((nextp, 0))
                # 把新的位置等压入栈
                if nextp == end:
                    # 发现新位置是终点，结束
                    return st
                break
    print("没有发现路径")
    return []

import matplotlib.pyplot as plt
import matplotlib

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号

st = st_find(maze, (1, 1), (8, 1))
x=[]
y=[]
for i in st:
    x.append(i[0][0])
    y.append(i[0][1])

plt.plot(x, y, 'r')
xq=[]
yq=[]
for i in range(10):
    for j in range(11):
        if maze[i, j] == 1:
            xq.append(i)
            yq.append(j)
plt.plot(xq, yq, '*')
plt.title('深度优先搜索找到迷宫的路径')
plt.show()
