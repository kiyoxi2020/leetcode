'''
作者：伏尔塔瓦尔河的纤夫
链接：https://www.nowcoder.com/discuss/640560?channel=-1&source_id=profile_follow_post_nctrack
来源：牛客网

反转字符串
题目
将()中的字符串翻转，并在输出中删除括号。

括号可迭代，如输入为 (uoy(love)i)，输出为(iloveyou)。

先翻转内层括号，再翻转外层括号。输出要删除掉所有括号。

'''

def compute(data):
    stack_letter = []
    stack_bracket = []
    for i in data:
        if i not in ['(', ')']:
            stack_letter.append(i)
        else:
            if len(stack_bracket) > 0 and i != stack_bracket[-1]:
                stack_bracket.pop(-1)
                t = []
                while(len(stack_letter)>0):
                    tt = stack_letter.pop(-1)
                    if tt == -1:
                        break
                    t.append(tt)
                for j in t:
                    stack_letter.append(j)
            else:
                stack_bracket.append(i)
                stack_letter.append(-1)
    print( ''.join(stack_letter))
    return


while(1):
    try:
        data = input()
        compute(data)
    except:
        break