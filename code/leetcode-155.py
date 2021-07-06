class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_sort = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.stack_sort) == 0 or self.stack_sort[-1]<val: 
            self.stack_sort.append(val)
        else:
            for i in range(len(self.stack_sort)):
                if self.stack_sort[i]>=val:
                    self.stack_sort.insert(i, val)
                    break
        return


    def pop(self):
        """
        :rtype: None
        """
        t = self.stack.pop(-1)
        self.stack_sort.remove(t)
        return


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_sort[0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()