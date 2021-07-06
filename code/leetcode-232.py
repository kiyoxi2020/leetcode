'''
leetcode 232. 用栈实现队列

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.stack2) == 0:
            while(len(self.stack1)!=0):
                self.stack2.append(self.stack1.pop(-1))
        self.stack1.append(x)
        return



    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2)!=0: 
            t = self.stack2.pop(-1)
            if len(self.stack2) == 0:
                while(len(self.stack1)!=0):
                    self.stack2.append(self.stack1.pop(-1))
            return t
        else:
            return self.stack1.pop(-1)


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2)!=0: 
            return self.stack2[-1]
        else:
            return self.stack1[-1]



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1)+len(self.stack2)==0: return True
        else: return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()