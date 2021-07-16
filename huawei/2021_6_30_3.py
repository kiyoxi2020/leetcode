
'''
三、逃出生天
在大小为row*col的方格区域地图上，处处暗藏杀机，地图上每一个格子均有一个倒计时转置，当时间变为0时会触发籍贯，使得该格子区域变为一处死地，该区域无法通过，英雄每移动一个格子消耗1s。英雄可以上下左右四个方向移动，请设置一条最佳路线，让英雄最短时间从[0,0]到达[row-1,col-1]离开。
注意：英雄在出生点和出口时，该区域不能为死地。

输入
首行输入单个空格分隔的两个正整数row和col，row代表行数（0<row<=15），col代表列数（0<col<=15）
接下来row行，每一行包含col个以当个空格分隔的数字，代表对应时间的区域倒计时装置设定时间time，单位为秒（0<=time<=100）

输出
英雄从起点到终点的最短用时，若无法到达，则输出-1

'''
def compute(matrix):
    row, col = len(matrix), len(matrix[0])
    searched = [[0] * col for _ in range(row)]
    path = []
    path_all = []

    def dfs(i, j, step, row, col, list0):
        if i == row-1 and j == col-1:
            path.append(step)
            path_all.append([i for i in list0])
            return
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            i_new = i + di
            j_new = j + dj
            if i_new >= 0 and i_new < row and j_new >= 0 and j_new < col and searched[i_new][j_new] == 0:
                if matrix[i_new][j_new] - step > 0:
                    searched[i_new][j_new] = 1
                    dfs(i_new, j_new, step+1, row, col, list0+[(i_new, j_new)])
                    searched[i_new][j_new] = 0
        return

    if matrix[0][0] == 0: 
        print(-1)
        return
    searched[0][0] = 1
    dfs(0, 0, 1, row, col, [(0, 0)])
    if len(path) > 0: print(min(path)-1)
    else: print(-1)
    return 


while(1):
    try:
        row, col = [int(i) for i in input().split(' ')]
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            data = [int(i) for i in input().split(' ')]
            for j in range(col):
                matrix[i][j] = data[j]
        compute(matrix)
    except:
        break