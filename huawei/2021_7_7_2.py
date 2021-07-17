'''
二、逛动物园
由于疫情影响，动物园进行人流管控，减少人员接触，因此从入口进入之后，只能选择某一条路单项行进，比如：老虎园的编码为1，是自愿的编码为2，猴子园的编码为3，天鹅园的编码为4，而从一个地方到另一个地方有一定的距离，则用一下结构表示：老虎园到狮子园，[1,2,15]，狮子园到猴子园[2,3,7]，猴子园到天鹅园[3,4,9]，现状随机拟定一个景点(S)作为出发点，判断是否可能逛完所有景点(N个)。若不能逛完返回-1，若可以逛完，则返回最长距离。
输入
前面每行表示2各景点的路线和距离，格式如[1,2,15]，表示景点1到景点2可通，距离为15。
倒数第2行为景点总数N，倒数第1行为S表示出发点。
————————————————
版权声明：本文为CSDN博主「柠檬の夏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Us006124/article/details/118654337

'''
def compute(dis, n, st):
    matrix = [[-1] * n for _ in range(n)]
    for i, j, d in dis:
        matrix[i-1][j-1] = d
        matrix[j-1][i-1] = d
    st -= 1
    searched = [0] * n
    searched[st] = 1
    out = [-1]

    def dfs(id, L, count, n):
        if count == n:
            out.append(L)
            return
        for i in range(n):
            if i!=id and matrix[i][id] != -1 and searched[i]==0:
                searched[i] = 1
                dfs(i, L+matrix[i][id], count+1, n)
                searched[i] = 0
        return
    
    dfs(st, 0, 1, n)
    print(max(out))
    return

while(1):
    try:
        dis = []
        n = 0
        st = 0
        while(1):
            data = input()
            if '[' in data:
                data = data[1:]
                data = data[:-1]
                data = [int(i) for i in data.split(',')]
                dis.append(data)
            else:
                n = int(data)
                st = int(input())
                break
        compute(dis, n, st)
    except:
        break
