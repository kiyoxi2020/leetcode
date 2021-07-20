def func(data):
    pos = {}
    n = 9
    for i in range(n):
        for j in range(n):
            if data[i][j]==0: 
                pos[(i,j)]=[]
    for i,j in pos.keys():
        for ii in range(i//3*3, i//3*3+3, 1):
            for jj in range(j//3*3, j//3*3+3,1):
                if data[ii][jj] != 0 and data[ii][jj] not in pos[(i,j)]:
                    pos[(i,j)].append(data[ii][jj])
        for ii in range(9):
            if data[ii][j] != 0 and data[ii][j] not in pos[(i,j)]:
                pos[(i,j)].append(data[ii][j])
        for jj in range(9):
            if data[i][jj] != 0 and data[i][jj] not in pos[(i,j)]:
                pos[(i,j)].append(data[i][jj])
            
    def dfs(ind):
        if len(pos)==ind: return True
        i, j = list(pos.keys())[ind]
        for k in range(1, 10, 1):
            if k not in pos[(i,j)]:
                data[i][j] = k
                rec = []
                for i0, j0 in list(pos.keys())[ind+1:]:
                    if i==i0 or j==j0 or ((i0-i//3*3)<3 and (i0-i//3*3)>=0 and (j0-j//3*3)<3 and (j0-j//3*3)>=0):
                        if k not in pos[(i0, j0)]:
                            pos[(i0, j0)].append(k)
                            rec.append([i0,j0])
                if dfs(ind+1): return True
                else:
                    data[i][j] = 0
                    for i0, j0 in rec:
                        pos[(i0,j0)].pop(-1)
                    
        return False
    
    dfs(0)
    return data

import sys
while(1):
    data = []
    for i in range(9):
        t = sys.stdin.readline()
        if t =='': break
        t = t.strip().split(' ')
        data.append([int(j) for j in t])
    out = func(data)
    print('----------------------------')
    for i in out:
        print(' '.join([str(k) for k in i]))
                            

# 5 3 0 0 7 0 0 0 0
# 6 0 0 1 9 5 0 0 0
# 0 9 8 0 0 0 0 6 0
# 8 0 0 0 6 0 0 0 3
# 4 0 0 8 0 3 0 0 1
# 7 0 0 0 2 0 0 0 6
# 0 6 0 0 0 0 2 8 0
# 0 0 0 4 1 9 0 0 5
# 0 0 0 0 8 0 0 7 9



# 7 2 6 9 0 4 0 5 1
# 0 8 0 6 0 7 4 3 2
# 3 4 1 0 8 5 0 0 9
# 0 5 2 4 6 8 0 0 7
# 0 3 7 0 0 0 6 8 0
# 0 9 0 0 0 3 0 1 0
# 0 0 0 0 0 0 0 0 0
# 9 0 0 0 2 1 5 0 0
# 8 0 0 3 0 0 0 0 0
            




