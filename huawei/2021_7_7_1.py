'''
一、工单调用策略
当小区通信设备上报警时，系统会自动生成待处理的工单，华为工单调度系统需要根据不同的策略，
调度外线工程师（FME）上站去修复工单对应的问题。
根据与运营商签订的合同，不同严重程度的工单被处理并修复的时长要求不同，
这个要求被修复的时长我们称之为SLA时间。假设华为与运营商A签订了运维合同，
部署了一套调度系统，只有1个外线工程师（FME），每个工单根据问题严重程度会给一个评分，
在SLA时间内完成修复的工单，华为员工获得工单对应的积分，超过SLA完成的工单不获得积分，
但必须完成该工单，运营商最终会根据积分付款。
请设计一种调度策略，根据现状得到调度结果完成所有工单，
让这个外线工程师处理的工单处理的工单获得的总积分最多。
假设从耨个调度时刻开始，当前工单数量N，不会产生新的工单，每个工单处理修复耗时为1小时。
请设计你的调度策略，完成业务目标。
————————————————
版权声明：本文为CSDN博主「柠檬の夏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Us006124/article/details/118654337
'''

def compute(data):
    data.sort(key=lambda x: x[0])
    t = [i[0] for i in data]
    v = [i[1] for i in data]
    n = len(t)
    m = max(t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[j][i] = max(dp[j][i], dp[j][i-1], dp[j-1][i])
            if t[i-1]>=j:
                dp[j][i] = max(dp[j][i], dp[j-1][i-1]+v[i-1])
    
    print(dp[m][n])
    return

while(1):
    n = int(input())
    data = []
    for i in range(n):
        t0, v0 = [int(i) for i in input().split()]
        data.append([t0, v0])
    compute(data)