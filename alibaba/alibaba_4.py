'''
小强在玩一个走迷宫的游戏，他操控的人物现在位于迷宫的起点，他的目标是尽快的到达终点。
每一次他可以选择花费一个时间单位向上或向下或向左或向右走一格，
或是使用自己的对称飞行器花费一个时间单位瞬移到关于当前自己点中心对称的格子，
且每一次移动的目的地不能存在障碍物。

具体来说，设当前迷宫有n行m列，
如果当前小强操控的人物位于点A(x,y)，
那么关于点A中心对称的格子B(x',y')满足x+x'=n+1且y+y'=m+1。
需要注意的是，对称飞行器最多使用5次。

示例1
输入
4 4
#S..
E#..
#...
....
输出
4

https://www.nowcoder.com/questionTerminal/ef231526f822489d879949226b4bed65
'''
import sys

def func(matrix, st):
    n, m = len(matrix), len(matrix[0])
    searched = [[0]*m for _ in range(n)]
    stack = [st]
    searched[st[0]][st[1]] = 1
    count = 0
    count_jump = [0]
    while(len(stack)>0):
        stack0 = []
        count_jump0 = []
        count += 1
        for [i, j], z in zip(stack, count_jump):
            flag = 0
            for i2, j2 in [[i-1,j],[i+1,j],[i,j+1],[i,j-1],[n-1-i,m-1-j]]:
                flag += 1
                if i2>=0 and i2<n and j2>=0 and j2<m:
                    if searched[i2][j2]==0 and matrix[i2][j2]!='#' and (not (z>=5 and flag>=5)) :
                        if matrix[i2][j2] == 'E': return count
                        searched[i2][j2] = 1
                        stack0.append([i2,j2])
                        if flag == 5:
                            count_jump0.append(z+1)
                        else:
                            count_jump0.append(z)
        stack = stack0
        count_jump = count_jump0
    return -1
    

n, m = map(int, sys.stdin.readline().strip().split(' '))
matrix = [['']*m for _ in range(n)]
st = []
ed = []
for i in range(n):
    data = sys.stdin.readline().strip()
    for j in range(m):
        matrix[i][j] = data[j]
        if data[j] == 'S': st = [i, j]
        elif data[j] == 'E': ed = [i, j]

print(func(matrix, st))


'''
4 4
#S..
E#..
#...
....


'''