'''
三、中国象棋
科科最近在学习中国象棋，今日的目标是钻研马走日，给定一张棋盘，棋盘上的棋子有三种类型，
马的起始位置，马要到达的目标位置和其他棋子，其他棋子可能会西安至马的前进路线，限制条件如下：

    马走日的路径上不能被绊马脚；
    马不能到达有棋子的位置。
    
科科是个象棋新手，请你帮他计算出到达目标位置至少要走多少步，如果不能到达输出-1.
马每次跳跃最多可以有8个方向，但如果前进方向有棋子，则会被绊马脚。
如下图，马的上方有棋子，则红色图形的点不能到达，五角星的位置是马可以到达的位置。
输入
棋盘宽度w(1≤w≤150)，棋盘高度h(1≤h≤150)
棋局，二维数组char[w][h]
其中，.表示没有棋子，#表示有棋子，H表示马当前的位置，T表示马要到达的位置。
输出
输出一个整数，代表马从H到达T最少需要的步数，没有路径则输出-1。
样例1
输入： 5 13
…H…#
…#…
…#…
.#…
…T#.
输出： 4
————————————————
版权声明：本文为CSDN博主「柠檬の夏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Us006124/article/details/118654337

'''
def compute(matrix, pos_st, pos_ed):
    direction = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [-2, 1], [-2, -1], [2, -1]]
    d_stop_pos = [[0, 1], [0, -1], [0, 1], [0, -1], [1, 0], [-1, 0], [-1, 0], [1, 0]]
    row, col = len(matrix), len(matrix[0]) 
    stack = []
    searched = [[0] * col for _ in range(row)]
    stack.append(pos_st)
    count = 0
    searched[pos_st[0]][pos_st[1]] = 1
    while(len(stack)>0):
        stack0 = []
        flag = 0
        for i, j in stack:
            if i == pos_ed[0] and j == pos_ed[1]:
                flag = 1
                break
            for d_ij, s_ij in zip(direction, d_stop_pos):
                i_new = d_ij[0] + i
                j_new = d_ij[1] + j
                i_stop = s_ij[0] + i
                j_stop = s_ij[1] + j
                if i_new >= 0 and i_new < row and j_new >= 0 and j_new < col:
                    if matrix[i_stop][j_stop] != '#' and searched[i_new][j_new] == 0:
                        stack0.append([i_new, j_new])
                        searched[i_new][j_new] = 1
        if flag == 1: break
        stack = stack0
        count += 1

    if count != 0: print(count)
    else: print('-1')
    return


while(1):
    row, col = [int(i) for i in input().split(' ')]
    matrix = [[''] * col for _ in range(row)]
    pos_st = []
    pos_ed = []
    for i in range(row):
        data = input()
        for j in range(col):
            if data[j] == 'H': pos_st = [i, j]
            if data[j] == 'T': pos_ed = [i, j]
            matrix[i][j] = data[j]
    compute(matrix, pos_st, pos_ed)

'''
5 13
........H...#
........#....
.....#.......
.#...........
..........T#.

5 13
........H...#
........#....
.....#.T.....
.#...........
...........#.

'''
