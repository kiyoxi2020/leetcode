'''
2.网络模型最小执行时间
题目大意：深度学习网络由若干算子组成，为简单起见，网络模型为有向无环图。若算子A依赖算子B，则仅当B执行完成之后才能执行A，没有依赖关系的算子可以并行执行。已知每个算子的执行时间，计算运行整个网络所需要的最小时间。

请注意：1、不考虑数据在算子之间的传输时间。2、第一个算子为输入算子且仅有一个输入算子。3、算
子索引从0开始。

输入
第一行为整数N，表示N（N<=100）个算子，接下来的N行为算子属性，分别表示算子名，算子运算时间，算子所指向的下一层算子索引。
如：
4
softmax 10 1 2
relu 5
conv 1 3
softmax 2

输出
15
————————————————
版权声明：本文为CSDN博主「Huntermanwp」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Huntermanwp/article/details/117981494
'''

def compute(node_time, node_to):
    n = len(node_time)

    def dfs(i, n, node_time, node_to):
        if i == n-1:
            return node_time[i]
        else:
            max0 = node_time[i]
            for j in range(len(node_to[i])):
                t = dfs(node_to[i][j], n, node_time, node_to) + node_time[i]
                max0 = max(max0, t)
            return max0                
    
    out = dfs(0, n, node_time, node_to)
    print(out)
    return


while(1):
    try:
        n = int(input())
        node_time = []
        node_to = []
        for _ in range(n):
            data = input().split(' ')
            node_time.append(int(data[1]))
            t = []
            for i in range(2, len(data)):
                t.append(int(data[i]))
            node_to.append(t)
        compute(node_time, node_to)
    except:
        break