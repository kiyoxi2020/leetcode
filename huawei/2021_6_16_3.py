'''
3.棋子搜索
题意：
给定一个围棋棋局，横竖19个旗子，用0表示空子，用1表示白子，2表示黑子，判断黑子连成一片的多还是白子连成一片的多。所谓连成一片指上下左右相邻，且中间不能有空子或者对方棋子。

输入：
19*19矩阵

输出：
第一行：白子连成一片的最大个数
第二行：黑子连成一片的最大个数
第三行：如果白子连成一片的最大个数大于黑子，输出white，否则输出black，如果相等，输出equal
————————————————
版权声明：本文为CSDN博主「Huntermanwp」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Huntermanwp/article/details/117981494
'''
def compute(matrix, n):
    max_white = 0
    max_black = 0
    searched = [[0] * n for _ in range(n)]

    def dfs(i, j, t, n):
        searched[i][j] = 1
        count = 1
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            i_new = i + di
            j_new = j + dj
            if i_new>=0 and i_new<n and j_new>=0 and j_new<n and searched[i_new][j_new] == 0:
                if matrix[i_new][j_new] == t:
                    count += dfs(i_new, j_new, t, n)
        return count

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and searched[i][j] == 0:
                t = dfs(i, j, 1, n)
                max_white = max(max_white, t)
            elif matrix[i][j] == 2 and searched[i][j] == 0:
                t = dfs(i, j, 2, n)
                max_black = max(max_black, t)
    print(max_white)
    print(max_black)
    if max_white > max_black: print('white')
    else: print('black')
    return
        

while(1):
    n = 5
    matrix = []
    for i in range(n):
        data = [int(i) for i in input().split(' ')]
        matrix.append(data)

    compute(matrix, n)
        